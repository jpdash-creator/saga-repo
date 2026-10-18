# ═══════════════════════════════════════════════════════════════════════════
# STARWARD SAGA — Phase and Section Image Creator
# Authorised Novel-Output Script #4 (guardrails/tools/guardrail-authorized-scripts-only.md)
# Commands: /create-image-phase and /create-image-section
#
# Three generation modes:
#   Mode A — OpenAI DALL-E (gpt-image-1 / dall-e-3)
#   Mode B — Stability AI (Stable Diffusion via REST API)
#   Mode C — Pure Python SVG (programmatic; uses AskUserQuestion input)
#
# Images saved as:
#   Phase:   novel-starward-saga/phase-N/phase-icon.png  +  phase-icon.svg
#   Section: novel-starward-saga/phase-N/section-N/section-icon.png  +  section-icon.svg
#
# Canon commands:
#   /create-image-phase   — generate / regenerate Phase N icon
#   /create-image-section — generate / regenerate Section N icon
#
# Usage (direct invocation from Gate 2 / command handler):
#   python saga_image_creator.py phase   --phase 1 --name "The Roots of Becoming" \
#          --prompt "..." --mode openai --output-root /path/to/novel-starward-saga
#
#   python saga_image_creator.py section --phase 1 --section 2 \
#          --name "Azure Sky and Gale" --prompt "..." \
#          --mode stability --output-root /path/to/novel-starward-saga
#
# AI invocation (via Gate 2 executor):
#   from saga_image_creator import generate_phase_image, generate_section_image
# ═══════════════════════════════════════════════════════════════════════════

from __future__ import annotations

import argparse
import base64
import io
import math
import os
import sys
import textwrap
from pathlib import Path
from typing import Optional


# ─── CANONICAL FILE NAMES ─────────────────────────────────────────────────
PHASE_PNG_NAME   = "phase-icon.png"
PHASE_SVG_NAME   = "phase-icon.svg"
SECTION_PNG_NAME = "section-icon.png"
SECTION_SVG_NAME = "section-icon.svg"

# ─── DEFAULT IMAGE DIMENSIONS ─────────────────────────────────────────────
DEFAULT_PNG_WIDTH  = 1024   # pixels — DALL-E / Stability AI standard
DEFAULT_PNG_HEIGHT = 1024
SVG_VIEWBOX_W      = 400    # SVG canvas — used for Python-generated SVGs
SVG_VIEWBOX_H      = 400

# ─── API ENVIRONMENT VARIABLES ────────────────────────────────────────────
OPENAI_KEY_ENV    = "OPENAI_API_KEY"
STABILITY_KEY_ENV = "STABILITY_API_KEY"

# ─── DEFAULT OUTPUT ROOT ──────────────────────────────────────────────────
def _default_output_root() -> str:
    """
    The novel output folder, computed from this script's own location so the images land in
    the same place whatever folder a session runs from (the method reset_story.py uses).
    This file lives at REPO_ROOT/.claude/tools/saga_image_creator.py, so two folders above the
    tools folder is REPO_ROOT and the output folder is REPO_ROOT/projects/novel-starward-saga.
    """
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(os.path.dirname(tools_dir))
    return os.path.join(repo_root, "projects", "novel-starward-saga")


DEFAULT_OUTPUT_ROOT = _default_output_root()


# ═══════════════════════════════════════════════════════════════════════════
# PATH HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def get_phase_icon_paths(phase: int, output_root: str) -> tuple[str, str]:
    """Return (png_path, svg_path) for a Phase icon."""
    folder = os.path.join(output_root, f"phase-{phase}")
    return (
        os.path.join(folder, PHASE_PNG_NAME),
        os.path.join(folder, PHASE_SVG_NAME),
    )


def get_section_icon_paths(phase: int, section: int, output_root: str) -> tuple[str, str]:
    """Return (png_path, svg_path) for a Section icon."""
    folder = os.path.join(output_root, f"phase-{phase}", f"section-{section}")
    return (
        os.path.join(folder, SECTION_PNG_NAME),
        os.path.join(folder, SECTION_SVG_NAME),
    )


# ═══════════════════════════════════════════════════════════════════════════
# MODE A — OPENAI DALL-E
# ═══════════════════════════════════════════════════════════════════════════

def _generate_openai(prompt: str, png_path: str) -> None:
    """
    Call OpenAI Images API (DALL-E 3 / gpt-image-1) and write PNG to png_path.
    API key read from OPENAI_API_KEY environment variable.
    """
    try:
        import openai                                            # type: ignore
    except ImportError:
        raise RuntimeError(
            "openai package not installed. Run: pip install openai"
        )

    api_key = os.environ.get(OPENAI_KEY_ENV)
    if not api_key:
        raise RuntimeError(
            f"OpenAI API key not found. Set {OPENAI_KEY_ENV} environment variable."
        )

    client = openai.OpenAI(api_key=api_key)

    # Prefer gpt-image-1 (newest); fall back to dall-e-3
    for model in ("gpt-image-1", "dall-e-3"):
        try:
            response = client.images.generate(
                model=model,
                prompt=prompt,
                size="1024x1024",
                response_format="b64_json",
                n=1,
            )
            image_data = base64.b64decode(response.data[0].b64_json)
            os.makedirs(os.path.dirname(png_path), exist_ok=True)
            with open(png_path, "wb") as f:
                f.write(image_data)
            print(f"  [OpenAI {model}] PNG written: {png_path}")
            return
        except Exception as exc:
            # If gpt-image-1 is unavailable, try dall-e-3
            if model == "gpt-image-1":
                print(f"  [OpenAI] gpt-image-1 unavailable ({exc}), trying dall-e-3...")
                continue
            raise RuntimeError(f"OpenAI image generation failed: {exc}") from exc


# ═══════════════════════════════════════════════════════════════════════════
# MODE B — STABILITY AI
# ═══════════════════════════════════════════════════════════════════════════

def _generate_stability(prompt: str, png_path: str) -> None:
    """
    Call Stability AI REST API and write PNG to png_path.
    API key read from STABILITY_API_KEY environment variable.
    """
    try:
        import requests                                          # type: ignore
    except ImportError:
        raise RuntimeError(
            "requests package not installed. Run: pip install requests"
        )

    api_key = os.environ.get(STABILITY_KEY_ENV)
    if not api_key:
        raise RuntimeError(
            f"Stability AI API key not found. Set {STABILITY_KEY_ENV} environment variable."
        )

    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    body = {
        "text_prompts": [{"text": prompt, "weight": 1.0}],
        "cfg_scale": 7,
        "width": DEFAULT_PNG_WIDTH,
        "height": DEFAULT_PNG_HEIGHT,
        "samples": 1,
        "steps": 30,
    }

    response = requests.post(url, headers=headers, json=body, timeout=120)
    if response.status_code != 200:
        raise RuntimeError(
            f"Stability AI API error {response.status_code}: {response.text[:400]}"
        )

    artifacts = response.json().get("artifacts", [])
    if not artifacts:
        raise RuntimeError("Stability AI returned no image artifacts.")

    image_data = base64.b64decode(artifacts[0]["base64"])
    os.makedirs(os.path.dirname(png_path), exist_ok=True)
    with open(png_path, "wb") as f:
        f.write(image_data)
    print(f"  [Stability AI] PNG written: {png_path}")


# ═══════════════════════════════════════════════════════════════════════════
# MODE C — PURE PYTHON SVG
# ═══════════════════════════════════════════════════════════════════════════

def _build_svg_from_user_input(
    name: str,
    tier_type: str,
    number: int,
    svg_params: dict,
) -> str:
    """
    Build an SVG string from user-supplied visual parameters.

    svg_params keys (all optional — defaults applied if absent):
        bg_color        : str  — hex or CSS color for background (default "#0D0D2B" deep navy)
        accent_color    : str  — hex or CSS color for accent rings/shapes (default "#4A8FDE")
        symbol_color    : str  — hex or CSS color for central symbol (default "#F2C94C" gold)
        title_color     : str  — hex or CSS color for text (default "#FFFFFF")
        shape           : str  — "mandala" | "star" | "rings" | "starfield" (default "mandala")
        ring_count      : int  — number of concentric rings for ring/mandala shapes (default 3)
        star_points     : int  — number of points for star shape (default 8)
        subtitle        : str  — optional subtitle line below name (default "")
    """
    bg       = svg_params.get("bg_color",      "#0D0D2B")
    accent   = svg_params.get("accent_color",  "#4A8FDE")
    symbol   = svg_params.get("symbol_color",  "#F2C94C")
    txt_col  = svg_params.get("title_color",   "#FFFFFF")
    shape    = svg_params.get("shape",         "mandala")
    rings    = int(svg_params.get("ring_count", 3))
    pts      = int(svg_params.get("star_points", 8))
    subtitle = svg_params.get("subtitle",      "")

    cx, cy  = SVG_VIEWBOX_W / 2, SVG_VIEWBOX_H / 2
    max_r   = min(cx, cy) * 0.72

    lines: list[str] = [
        f'<svg viewBox="0 0 {SVG_VIEWBOX_W} {SVG_VIEWBOX_H}" '
        f'xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink">',
        f'  <defs>',
        f'    <radialGradient id="bgGrad" cx="50%" cy="50%" r="70%">',
        f'      <stop offset="0%" stop-color="{bg}" stop-opacity="1"/>',
        f'      <stop offset="100%" stop-color="{_darken(bg)}" stop-opacity="1"/>',
        f'    </radialGradient>',
        f'    <radialGradient id="glowGrad" cx="50%" cy="50%" r="50%">',
        f'      <stop offset="0%" stop-color="{symbol}" stop-opacity="0.35"/>',
        f'      <stop offset="100%" stop-color="{symbol}" stop-opacity="0"/>',
        f'    </radialGradient>',
        f'  </defs>',
        # Background
        f'  <rect width="{SVG_VIEWBOX_W}" height="{SVG_VIEWBOX_H}" fill="url(#bgGrad)"/>',
        # Glow halo
        f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{max_r * 0.9:.1f}" fill="url(#glowGrad)"/>',
    ]

    # ── Shape ────────────────────────────────────────────────────────────
    if shape == "rings" or shape == "mandala":
        for i in range(rings, 0, -1):
            r     = max_r * (i / rings) * 0.95
            sw    = max(1, 3 - i * 0.4)
            alpha = 0.20 + (i / rings) * 0.50
            lines.append(
                f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" '
                f'fill="none" stroke="{accent}" stroke-width="{sw:.1f}" '
                f'stroke-opacity="{alpha:.2f}"/>'
            )
        if shape == "mandala":
            # Radial lines
            for k in range(12):
                angle = math.radians(k * 30)
                x1 = cx + math.cos(angle) * (max_r * 0.18)
                y1 = cy + math.sin(angle) * (max_r * 0.18)
                x2 = cx + math.cos(angle) * (max_r * 0.78)
                y2 = cy + math.sin(angle) * (max_r * 0.78)
                lines.append(
                    f'  <line x1="{x1:.1f}" y1="{y1:.1f}" '
                    f'x2="{x2:.1f}" y2="{y2:.1f}" '
                    f'stroke="{accent}" stroke-width="0.8" stroke-opacity="0.4"/>'
                )

    elif shape == "star":
        outer_r = max_r * 0.82
        inner_r = max_r * 0.38
        poly_pts = []
        for k in range(pts):
            outer_a = math.radians(k * 360 / pts - 90)
            inner_a = math.radians((k + 0.5) * 360 / pts - 90)
            poly_pts.append(f"{cx + outer_r * math.cos(outer_a):.1f},"
                            f"{cy + outer_r * math.sin(outer_a):.1f}")
            poly_pts.append(f"{cx + inner_r * math.cos(inner_a):.1f},"
                            f"{cy + inner_r * math.sin(inner_a):.1f}")
        lines.append(
            f'  <polygon points="{" ".join(poly_pts)}" '
            f'fill="{symbol}" fill-opacity="0.20" '
            f'stroke="{accent}" stroke-width="1.5"/>'
        )

    elif shape == "starfield":
        import random
        rng = random.Random(number * 997 + len(name))
        for _ in range(60):
            sx = rng.uniform(10, SVG_VIEWBOX_W - 10)
            sy = rng.uniform(10, SVG_VIEWBOX_H - 10)
            sr = rng.uniform(0.5, 2.5)
            sa = rng.uniform(0.3, 1.0)
            lines.append(
                f'  <circle cx="{sx:.1f}" cy="{sy:.1f}" r="{sr:.1f}" '
                f'fill="{txt_col}" fill-opacity="{sa:.2f}"/>'
            )
        # Nebula blobs
        for _ in range(4):
            nx = rng.uniform(80, SVG_VIEWBOX_W - 80)
            ny = rng.uniform(80, SVG_VIEWBOX_H - 80)
            nr = rng.uniform(40, 90)
            lines.append(
                f'  <circle cx="{nx:.1f}" cy="{ny:.1f}" r="{nr:.1f}" '
                f'fill="{accent}" fill-opacity="0.07"/>'
            )

    # ── Central symbol: inner ring + number glyph ─────────────────────────
    lines.append(
        f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{max_r * 0.22:.1f}" '
        f'fill="{symbol}" fill-opacity="0.15" stroke="{symbol}" stroke-width="2"/>'
    )
    tier_label = f"{tier_type.upper()} {number}"
    lines.append(
        f'  <text x="{cx:.1f}" y="{cy - max_r * 0.04:.1f}" '
        f'text-anchor="middle" dominant-baseline="middle" '
        f'font-family="Georgia, \'Times New Roman\', serif" '
        f'font-size="18" font-weight="bold" fill="{symbol}" fill-opacity="0.9">'
        f'{tier_label}</text>'
    )

    # ── Title text ────────────────────────────────────────────────────────
    wrapped = textwrap.wrap(name, width=22)
    title_y_start = cy + max_r * 0.38
    line_h = 22
    for idx, wline in enumerate(wrapped[:3]):
        lines.append(
            f'  <text x="{cx:.1f}" y="{title_y_start + idx * line_h:.1f}" '
            f'text-anchor="middle" '
            f'font-family="Georgia, \'Times New Roman\', serif" '
            f'font-size="16" fill="{txt_col}" fill-opacity="0.95">'
            f'{_escape_xml(wline)}</text>'
        )
    if subtitle:
        sub_y = title_y_start + len(wrapped[:3]) * line_h + 6
        lines.append(
            f'  <text x="{cx:.1f}" y="{sub_y:.1f}" '
            f'text-anchor="middle" '
            f'font-family="Georgia, \'Times New Roman\', serif" '
            f'font-size="12" font-style="italic" fill="{txt_col}" fill-opacity="0.70">'
            f'{_escape_xml(subtitle)}</text>'
        )

    lines.append("</svg>")
    return "\n".join(lines)


def _darken(hex_color: str) -> str:
    """Return a darkened version of a hex color (for gradient bottom)."""
    h = hex_color.lstrip("#")
    if len(h) == 6:
        try:
            r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
            r, g, b = max(0, r - 30), max(0, g - 30), max(0, b - 30)
            return f"#{r:02X}{g:02X}{b:02X}"
        except ValueError:
            pass
    return hex_color


def _escape_xml(text: str) -> str:
    """Escape XML special characters."""
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


def _svg_to_png(svg_path: str, png_path: str) -> bool:
    """
    Attempt to convert SVG to PNG using cairosvg (if installed).
    Returns True on success, False when cairosvg is missing or the conversion fails
    (the caller then raises and writes nothing).
    """
    try:
        import cairosvg                                          # type: ignore
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=DEFAULT_PNG_WIDTH,
            output_height=DEFAULT_PNG_HEIGHT,
        )
        return True
    except ImportError:
        return False
    except Exception as exc:
        print(f"  [SVG to PNG] cairosvg conversion failed: {exc}", file=sys.stderr)
        return False


# An icon PNG is far larger than this.
MIN_PNG_BYTES = 1024


def _check_png_size(png_path: str) -> None:
    """Raise RuntimeError when the PNG is missing or is not over 1 KB (a blank or broken image)."""
    size = os.path.getsize(png_path) if os.path.exists(png_path) else 0
    if size <= MIN_PNG_BYTES:
        raise RuntimeError(
            f"{png_path} is {size} bytes; an icon PNG must be over {MIN_PNG_BYTES} bytes. "
            "Nothing was written and any icon already on disk is unchanged."
        )


def _generate_svg_mode(
    name: str,
    tier_type: str,
    number: int,
    svg_params: dict,
    png_path: str,
    svg_path: str,
) -> None:
    """
    Generate the SVG and the PNG using pure Python. Both files are written or neither is: they are
    made under temporary names, the PNG is checked, and only then are they moved into place. When
    cairosvg is missing or the PNG is not over 1 KB this raises RuntimeError, and any icon already
    on disk is left as it was. No placeholder PNG is ever written.
    """
    svg_content = _build_svg_from_user_input(name, tier_type, number, svg_params)
    os.makedirs(os.path.dirname(svg_path), exist_ok=True)
    tmp_svg, tmp_png = svg_path + ".part", png_path + ".part"
    try:
        with open(tmp_svg, "w", encoding="utf-8") as f:
            f.write(svg_content)
        if not _svg_to_png(tmp_svg, tmp_png):
            raise RuntimeError(
                "The PNG could not be made from the SVG (cairosvg is missing or failed). "
                "Nothing was written and any icon already on disk is unchanged. "
                "Install it with: pip install cairosvg"
            )
        _check_png_size(tmp_png)
        os.replace(tmp_svg, svg_path)
        os.replace(tmp_png, png_path)
    finally:
        for leftover in (tmp_svg, tmp_png):
            if os.path.exists(leftover):
                os.remove(leftover)
    print(f"  [SVG] Written: {svg_path}")
    print(f"  [SVG to PNG] Written: {png_path}")


# ═══════════════════════════════════════════════════════════════════════════
# PUBLIC API — PHASE IMAGE
# ═══════════════════════════════════════════════════════════════════════════

def generate_phase_image(
    phase: int,
    phase_name: str,
    prompt: str,
    output_root: str,
    mode: str = "openai",
    svg_params: Optional[dict] = None,
) -> tuple[str, str]:
    """
    Generate Phase icon images.  Called by /create-image-phase.

    Args:
        phase       : Phase number (integer ≥ 1)
        phase_name  : Human-readable Phase name (from Part 30 canon)
        prompt      : Image description (user-confirmed; see the Decision Consultation Gate, Part 28 Area 19)
        output_root : Path to novel-starward-saga/ directory
        mode        : "openai" | "stability" | "svg"
        svg_params  : Visual parameters for SVG mode (see _build_svg_from_user_input)

    Returns:
        (png_path, svg_path) — paths to the written files.
        PNG path is always populated: the SVG mode raises RuntimeError and writes nothing when
        cairosvg is missing or the PNG is not over 1 KB, so no placeholder is ever written.
        SVG path is always populated for SVG mode; empty string for API modes.
    """
    png_path, svg_path = get_phase_icon_paths(phase, output_root)
    os.makedirs(os.path.dirname(png_path), exist_ok=True)

    mode = mode.lower().strip()
    print(f"\nGenerating Phase {phase} image: '{phase_name}' | mode={mode}")

    if mode == "openai":
        _generate_openai(prompt, png_path)
        svg_path_out = ""
    elif mode == "stability":
        _generate_stability(prompt, png_path)
        svg_path_out = ""
    elif mode == "svg":
        params = svg_params or {}
        _generate_svg_mode(phase_name, "Phase", phase, params, png_path, svg_path)
        svg_path_out = svg_path
    else:
        raise ValueError(
            f"Unknown mode '{mode}'. Expected: 'openai' | 'stability' | 'svg'."
        )

    print(f"Phase {phase} image complete.")
    return png_path, svg_path_out


# ═══════════════════════════════════════════════════════════════════════════
# PUBLIC API — SECTION IMAGE
# ═══════════════════════════════════════════════════════════════════════════

def generate_section_image(
    phase: int,
    section: int,
    section_name: str,
    prompt: str,
    output_root: str,
    mode: str = "openai",
    svg_params: Optional[dict] = None,
) -> tuple[str, str]:
    """
    Generate Section icon images.  Called by /create-image-section.

    Args:
        phase        : Phase number (integer ≥ 1)
        section      : Section number within the Phase (integer ≥ 1)
        section_name : Human-readable Section name (from Part 30 canon)
        prompt       : Image description (user-confirmed; see the Decision Consultation Gate, Part 28 Area 19)
        output_root  : Path to novel-starward-saga/ directory
        mode         : "openai" | "stability" | "svg"
        svg_params   : Visual parameters for SVG mode

    Returns:
        (png_path, svg_path) — paths to the written files.
    """
    png_path, svg_path = get_section_icon_paths(phase, section, output_root)
    os.makedirs(os.path.dirname(png_path), exist_ok=True)

    mode = mode.lower().strip()
    print(f"\nGenerating Section {section} image: '{section_name}' | mode={mode}")

    if mode == "openai":
        _generate_openai(prompt, png_path)
        svg_path_out = ""
    elif mode == "stability":
        _generate_stability(prompt, png_path)
        svg_path_out = ""
    elif mode == "svg":
        params = svg_params or {}
        _generate_svg_mode(section_name, "Section", section, params, png_path, svg_path)
        svg_path_out = svg_path
    else:
        raise ValueError(
            f"Unknown mode '{mode}'. Expected: 'openai' | 'stability' | 'svg'."
        )

    print(f"Section {section} image complete.")
    return png_path, svg_path_out


# ═══════════════════════════════════════════════════════════════════════════
# CANON PROMPT BUILDER (DCG flow — AI auto-drafts, user confirms)
# ═══════════════════════════════════════════════════════════════════════════

def build_phase_prompt(phase: int, phase_name: str, phase_description: str = "") -> str:
    """
    Auto-draft an image prompt for a Phase icon from Part 30 canon context.
    The AI calls this, presents the result to the user via AskUserQuestion,
    and the user confirms or edits before the API is called.

    Args:
        phase             : Phase number
        phase_name        : Phase canonical name (Part 30)
        phase_description : Optional Phase thematic summary (Part 30)
    """
    base = (
        f"Epic fantasy cultivation novel cover art for Phase {phase}: '{phase_name}'. "
        "Celestial-themed, cosmic energy, cultivation power symbols. "
        "Deep space background with star clusters and nebulae. "
        "Central mandala of cultivation energy rings. Dramatic lighting. "
        "No text, no letters, no words. Square format."
    )
    if phase_description:
        thematic = phase_description[:200].strip()
        base += f" Thematic essence: {thematic}"
    return base


def build_section_prompt(
    phase: int,
    section: int,
    section_name: str,
    section_description: str = "",
) -> str:
    """
    Auto-draft an image prompt for a Section icon from Part 30 canon context.
    """
    base = (
        f"Fantasy cultivation novel chapter art for Section {section}: '{section_name}' "
        f"(within Phase {phase}). "
        "Location-anchored atmospheric art — conveys the dominant setting and arc. "
        "Cultivation energy, architectural grandeur, and emotional resonance. "
        "Deep color palette. No text, no letters, no words. Square format."
    )
    if section_description:
        thematic = section_description[:200].strip()
        base += f" Setting essence: {thematic}"
    return base


# ═══════════════════════════════════════════════════════════════════════════
# CLI ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

def _parse_svg_params(raw: list[str]) -> dict:
    """
    Parse key=value pairs from CLI --svg-param arguments.
    Example: --svg-param bg_color=#1A0A2E --svg-param shape=mandala
    """
    params = {}
    for item in raw:
        if "=" in item:
            k, v = item.split("=", 1)
            # Attempt int conversion for numeric params
            if v.isdigit():
                params[k.strip()] = int(v)
            else:
                params[k.strip()] = v
    return params


def main() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")   # a printed title or path never crashes the run
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(
        description="Starward Saga — Phase and Section Image Creator"
    )
    subparsers = parser.add_subparsers(dest="target", required=True)

    # ── phase subcommand ──────────────────────────────────────────────────
    phase_p = subparsers.add_parser("phase", help="Generate Phase image")
    phase_p.add_argument("--phase",       type=int,  required=True, help="Phase number")
    phase_p.add_argument("--name",        type=str,  required=True, help="Phase name")
    phase_p.add_argument("--prompt",      type=str,  default="",    help="Image prompt (empty = auto-draft)")
    phase_p.add_argument("--mode",        type=str,  default="openai",
                         choices=["openai", "stability", "svg"],
                         help="Image generation mode")
    phase_p.add_argument("--output-root", type=str,  default=DEFAULT_OUTPUT_ROOT,
                         help="Root output directory (default: REPO_ROOT/projects/novel-starward-saga, "
                              "computed from this script's location)")
    phase_p.add_argument("--svg-param",   type=str,  action="append", default=[],
                         metavar="KEY=VALUE", help="SVG visual parameter (repeatable)")
    phase_p.add_argument("--description", type=str,  default="",
                         help="Phase thematic description from Part 30 (used to auto-draft prompt)")

    # ── section subcommand ────────────────────────────────────────────────
    sec_p = subparsers.add_parser("section", help="Generate Section image")
    sec_p.add_argument("--phase",        type=int,  required=True, help="Parent Phase number")
    sec_p.add_argument("--section",      type=int,  required=True, help="Section number")
    sec_p.add_argument("--name",         type=str,  required=True, help="Section name")
    sec_p.add_argument("--prompt",       type=str,  default="",    help="Image prompt (empty = auto-draft)")
    sec_p.add_argument("--mode",         type=str,  default="openai",
                       choices=["openai", "stability", "svg"],
                       help="Image generation mode")
    sec_p.add_argument("--output-root",  type=str,  default=DEFAULT_OUTPUT_ROOT,
                       help="Root output directory (default: REPO_ROOT/projects/novel-starward-saga, "
                            "computed from this script's location)")
    sec_p.add_argument("--svg-param",    type=str,  action="append", default=[],
                       metavar="KEY=VALUE", help="SVG visual parameter (repeatable)")
    sec_p.add_argument("--description",  type=str,  default="",
                       help="Section description from Part 30 (used to auto-draft prompt)")

    args = parser.parse_args()

    if args.target == "phase":
        prompt = args.prompt or build_phase_prompt(args.phase, args.name, args.description)
        print(f"\n[Prompt used]:\n  {prompt}\n")
        svg_params = _parse_svg_params(args.svg_param)
        png_path, svg_path = generate_phase_image(
            phase=args.phase,
            phase_name=args.name,
            prompt=prompt,
            output_root=args.output_root,
            mode=args.mode,
            svg_params=svg_params if args.mode == "svg" else None,
        )
        print(f"\nResult: PNG={png_path or '(none)'} | SVG={svg_path or '(none)'}")

    elif args.target == "section":
        prompt = args.prompt or build_section_prompt(
            args.phase, args.section, args.name, args.description
        )
        print(f"\n[Prompt used]:\n  {prompt}\n")
        svg_params = _parse_svg_params(args.svg_param)
        png_path, svg_path = generate_section_image(
            phase=args.phase,
            section=args.section,
            section_name=args.name,
            prompt=prompt,
            output_root=args.output_root,
            mode=args.mode,
            svg_params=svg_params if args.mode == "svg" else None,
        )
        print(f"\nResult: PNG={png_path or '(none)'} | SVG={svg_path or '(none)'}")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
