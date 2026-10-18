#!/usr/bin/env python3
"""manual_ledger_query.py -- canon script 5: the read-only Manual Ledger query and validation tool (Part 42).

READ-ONLY. Standard library only. No network. It never writes, creates, edits, moves or deletes any file.
It reads the CSV files under  .claude/story-memory/ledger-manuals/  and prints results to stdout.
It is never called to produce Area text (guardrails/tools/guardrail-authorized-scripts-only.md).

Commands (Part 42 Rule 42.10.9.1 and the recommended sixth command, Rule 42.10.9.2):
  manual ID          a manual row (generic MAN-, kingdom AZ-/GA-/BR-, personal PER-, found FND-) with its kingdom
                     rows and the count of its move rows
  moves ID           the move rows of a manual ID, in order, or the one row of a move ID
  kit CHARACTER      the kit rows of a character with each manual's title, grade and band
  usable CHARACTER   Usable / Conditional / Latent for each move of each manual in the kit (Rule 42.3.3.1),
                     plus the informational eligibility test (Rule 42.11.6.1)
  validate           ledger checks C-1 to C-22 (weapon axis) and C-23 to C-31 (cultivation axis), FAIL lines and
                     INFO lines; exit code 1 on any FAIL
  find-name TEXT     every move name and manual title equal or close to TEXT (comparison form of check C-13)
  stats              counts of what exists, what is expected, and what is not yet generated
  affinity CODE      a cultivation discipline (affinities.csv row or design class), expected and present counts by grade

The cultivation axis lives in  <root>/cultivation/  (Canon Amendment 2026-10-16, _design-cultivation-axis.md). Missing or
partial cultivation files are reported as counts (INFO lines in the summary) and are never a FAIL until a file exists.

Option:  --axis weapon|cultivation|both   which axis validate / stats / find-name / usable cover (default both)
         --root PATH   use another ledger-manuals folder (for fixtures); default is the folder beside this script's
                       parent: <repo>/.claude/story-memory/ledger-manuals

Exit codes: 0 ok, 1 validation problems found, 2 usage error or ID / character not found.
"""

import sys

sys.dont_write_bytecode = True  # read-only tool: not even .pyc files

import argparse
import csv
import datetime
import difflib
import io
import re
from pathlib import Path

# ---------------------------------------------------------------------------------------------------------------
# Constants copied from Part 42 (the skill stands on any difference)
# ---------------------------------------------------------------------------------------------------------------

GRADE_FOLDERS = ["basic", "intermediate", "advanced", "elite", "signature", "fusion", "catastrophic", "mythic"]
GRADE_CODES = ["BAS", "INT", "ADV", "ELI", "SIG", "FUS", "CAT", "MYT"]
CODE_TO_FOLDER = dict(zip(GRADE_CODES, GRADE_FOLDERS))
FOLDER_TO_CODE = dict(zip(GRADE_FOLDERS, GRADE_CODES))
STOCK_GRADES = ["BAS", "INT", "ADV", "ELI", "SIG"]          # generated generic stock
HEADER_ONLY_GRADES = ["FUS", "CAT", "MYT"]                  # Rule 42.10.1.4
MOVE_TYPES = ["Basic", "Intermediate", "Advanced", "Elite", "Signature", "Fusion", "Catastrophic", "Mythic"]
TYPE_LETTER = dict(zip(MOVE_TYPES, "BIAESFCM"))
LETTER_TYPE = {v: k for k, v in TYPE_LETTER.items()}
TYPE_RANK = {t: i for i, t in enumerate(MOVE_TYPES)}
TYPE_BY_CODE = dict(zip(GRADE_CODES, MOVE_TYPES))           # BAS -> Basic, etc. (blocked_types codes)

H_WEAPONS = "weapon_id,family,name,description,prominence,basic_n,inter_n,adv_n,adv_common_n,adv_kingdom_n,elite_n,sig_n"
H_MANUALS = ("manual_id,grade,weapon_id,origin,title,realm_band,min_realm,energy_req,cultivation_req,affinity_req,"
             "sovereignty_req,move_count,composition,tradition,summary,status,first_area,notes")
H_MOVES = "move_id,manual_id,seq,name,move_type,function,form,cost_class,unlock_realm,description,status,first_area"
H_KINGDOM = "kingdom_id,manual_id,kingdom,institution,channel,access,copy_control,local_note,status"
H_PERSONAL = ("manual_id,grade,weapon_id,origin,title,realm_band,min_realm,energy_req,cultivation_req,affinity_req,"
              "sovereignty_req,move_count,composition,tradition,summary,owner,source,status,first_area,notes")
H_CHARS = "char_id,name,ledger_file,tier,kingdom,realm,effective_realm,blocked_types,affinity,sovereignty,primary_weapons,snapshot_date"
H_KITS = "char_id,manual_id,kingdom_manual_id,source,learned_via,mastery,assign_status,note"

# Rule 42.2.3.2 -- the composition table, fixed text copy: N -> cell per grade (BAS INT ADV ELI SIG FUS CAT MYT)
_COMP_TEXT = """
5|B5|B3 I2|B2 I2 A1|B2 I1 A1 E1|B1 I1 A1 E1 S1|B1 I1 A1 E1 F1|I1 A1 E1 S1 C1|A1 E1 S1 C1 M1
6|B6|B4 I2|B3 I2 A1|B2 I2 A1 E1|B1 I2 A1 E1 S1|B1 I2 A1 E1 F1|I1 A2 E1 S1 C1|A1 E2 S1 C1 M1
7|B7|B5 I2|B4 I2 A1|B3 I2 A1 E1|B2 I2 A1 E1 S1|B2 I2 A1 E1 F1|I2 A2 E1 S1 C1|A2 E2 S1 C1 M1
8|B8|B6 I2|B4 I2 A2|B3 I2 A2 E1|B2 I2 A2 E1 S1|B2 I2 A2 E1 F1|I2 A2 E2 S1 C1|A2 E2 S2 C1 M1
9|B9|B6 I3|B4 I3 A2|B3 I3 A2 E1|B2 I3 A2 E1 S1|B2 I3 A2 E1 F1|I2 A3 E2 S1 C1|A2 E3 S2 C1 M1
10|B10|B7 I3|B5 I3 A2|B4 I3 A2 E1|B3 I3 A2 E1 S1|B3 I3 A2 E1 F1|I3 A3 E2 S1 C1|A3 E3 S2 C1 M1
11|B11|B8 I3|B6 I3 A2|B5 I3 A2 E1|B3 I4 A2 E1 S1|B3 I4 A2 E1 F1|I3 A4 E2 S1 C1|A3 E4 S2 C1 M1
12|B12|B8 I4|B6 I4 A2|B5 I4 A2 E1|B4 I4 A2 E1 S1|B4 I4 A2 E1 F1|I4 A4 E2 S1 C1|A4 E4 S2 C1 M1
13|B13|B9 I4|B6 I4 A3|B5 I4 A3 E1|B4 I4 A3 E1 S1|B4 I4 A3 E1 F1|I4 A4 E3 S1 C1|A4 E4 S3 C1 M1
14|B14|B10 I4|B7 I4 A3|B6 I4 A3 E1|B4 I4 A3 E1 S2|B4 I4 A3 E1 F2|I4 A4 E3 S1 C2|A4 E4 S3 C1 M2
15|B15|B10 I5|B7 I5 A3|B6 I4 A3 E2|B4 I4 A3 E2 S2|B4 I4 A3 E2 F2|I4 A4 E3 S2 C2|A4 E4 S3 C2 M2
"""
COMPOSITION = {}
for _line in _COMP_TEXT.strip().splitlines():
    _p = _line.split("|")
    for _g, _cell in zip(GRADE_CODES, _p[1:]):
        COMPOSITION[(_g, int(_p[0]))] = _cell

# Rule 42.2.2.2 -- move-count ranges by grade
COUNT_RANGE = {"BAS": (5, 8), "INT": (6, 10), "ADV": (8, 12), "ELI": (9, 13),
               "SIG": (10, 12), "FUS": (10, 14), "CAT": (13, 15), "MYT": (12, 15)}

# Rule 42.2.3.1 -- the rounding rule (kept so the table can be cross-checked against its own rule)
GRADE_PERCENTS = {
    "BAS": {"Basic": 100},
    "INT": {"Basic": 70, "Intermediate": 30},
    "ADV": {"Basic": 50, "Intermediate": 30, "Advanced": 20},
    "ELI": {"Basic": 40, "Intermediate": 30, "Advanced": 20, "Elite": 10},
    "SIG": {"Basic": 30, "Intermediate": 30, "Advanced": 20, "Elite": 10, "Signature": 10},
    "FUS": {"Basic": 30, "Intermediate": 30, "Advanced": 20, "Elite": 10, "Fusion": 10},
    "CAT": {"Intermediate": 30, "Advanced": 30, "Elite": 20, "Signature": 10, "Catastrophic": 10},
    "MYT": {"Advanced": 30, "Elite": 30, "Signature": 20, "Catastrophic": 10, "Mythic": 10},
}


def rounded_composition(grade, n):
    pct = GRADE_PERCENTS[grade]
    types = sorted(pct, key=lambda t: TYPE_RANK[t])
    base = {t: (n * pct[t]) // 100 for t in types}
    left = n - sum(base.values())
    rem = {t: (n * pct[t]) % 100 for t in types}
    order = sorted(types, key=lambda t: (-rem[t], -TYPE_RANK[t]))  # tie goes to the HIGHER type
    for t in order[:left]:
        base[t] += 1
    if n >= len(types):
        for t in types:
            if base[t] < 1:
                big = max(base.values())
                donor = [x for x in types if base[x] == big][0]  # tie: LOWEST type
                base[donor] -= 1
                base[t] += 1
    return " ".join(f"{TYPE_LETTER[t]}{base[t]}" for t in types if base[t] > 0)


# Rule 42.3.2.1 / 42.3.2.2 -- access groups and matrix
REALMS = ["T1", "Senior", "Warrior", "Champion", "Ruler", "Monarch", "Demigod", "Void God", "True God",
          "Absolute God", "Core Formation", "Core Assimilation", "Core Solidification", "Divine Transformation",
          "Sea Formation", "Heaven Treading", "Divine Ascension", "Divine Sea Realm"]
REALM_INDEX = {r: i for i, r in enumerate(REALMS)}
T1_STAGES = ["Unawakened", "Skin", "Muscle", "Tendon", "Bone", "Blood", "Marrow", "Soul"]
REALM_TO_AG = {
    "T1": 1, "Senior": 2, "Warrior": 2, "Champion": 3, "Ruler": 3, "Monarch": 4, "Demigod": 5, "Void God": 5,
    "True God": 6, "Absolute God": 6, "Core Formation": 7, "Core Assimilation": 7, "Core Solidification": 8,
    "Divine Transformation": 9, "Sea Formation": 9, "Heaven Treading": 9, "Divine Ascension": 9,
    "Divine Sea Realm": 9,
}
ACCESS_MATRIX = {  # cells for AG1..AG9
    "Basic": "SSSSSSSSS", "Intermediate": "RSSSSSSSS", "Advanced": "--PPSSSSS", "Elite": "---RSSSSS",
    "Signature": "RPPPSSSSS", "Fusion": "---RPPSSS", "Catastrophic": "----PSSSS", "Mythic": "-----RPSS",
}
COND_CODE = {("Intermediate", 1): "C-T1-SPEC", ("Signature", 1): "C-T1-EXC", ("Elite", 4): "C-M-ELITE",
             ("Fusion", 4): "C-M-FUSION", ("Mythic", 6): "C-AG-MYTHIC"}
UNLOCK_REALM = {"Basic": "T1 Unawakened", "Intermediate": "Senior L1 Low", "Advanced": "Champion L1 Low",
                "Elite": "Demigod L1 Low", "Signature": "Senior L1 Low", "Fusion": "Demigod L1 Low",
                "Catastrophic": "Demigod L1 Low", "Mythic": "Core Formation L1 Low"}

BANDS = ["M1", "M2", "XT", "CF", "DV"]
# Rule 42.5.3.3 -- windows (grade, band) -> (low, high), each a list for exceptions
WINDOWS = {
    ("BAS", "M1"): [("T1 Unawakened", "T1 Bone")],
    ("BAS", "M2"): [("Senior L1 Low", "Senior L9 Peak")],
    ("INT", "M2"): [("Senior L1 Low", "Warrior L9 Peak")],
    ("INT", "M1"): [("T1 Marrow", "T1 Soul")],
    ("ADV", "M2"): [("Champion L1 Low", "Ruler L9 Peak")],
    ("ADV", "XT"): [("Demigod L1 Low", "Void God L9 Peak")],
    ("ELI", "XT"): [("Demigod L1 Low", "True God L9 Peak")],
    ("ELI", "M2"): [("Monarch L1 Low", "Monarch L9 Peak")],
    ("SIG", "M2"): [("Warrior L1 Low", "Ruler L1 Mid")],
    ("SIG", "XT"): [("Demigod L1 Low", "Void God L9 Peak")],
    ("SIG", "CF"): [("Core Formation L1 Low", "Core Assimilation L9 Peak")],
    ("FUS", "XT"): [("Demigod L1 Low", "Absolute God L9 Peak")],
    ("FUS", "CF"): [("Core Formation L1 Low", "Core Solidification L9 Peak")],
    ("CAT", "XT"): [("Demigod L1 Low", "Absolute God L9 Peak")],
    ("CAT", "CF"): [("Core Formation L1 Low", "Core Solidification L9 Peak")],
    ("CAT", "DV"): [("Divine Transformation L1 Low", "Divine Sea Realm L9 Peak")],
    ("MYT", "CF"): [("Core Formation L1 Low", "Core Solidification L9 Peak")],
    ("MYT", "DV"): [("Divine Transformation L1 Low", "Divine Sea Realm L9 Peak")],
}

ENERGY_LADDER = ["NONE", "QI-MIN", "QI-LOW", "QI-MOD", "QI-HIGH", "QI-VHI", "QI-EXT", "QI-REAL"]
AG_HIGHEST_ENERGY = {1: "NONE", 2: "QI-MOD", 3: "QI-MOD", 4: "QI-HIGH", 5: "QI-EXT", 6: "QI-EXT", 7: "QI-REAL",
                     8: "QI-REAL", 9: "QI-REAL"}
CULT_STATES = ["NONE", "T1-SKIN", "T1-MUSCLE", "T1-TENDON", "T1-BONE", "T1-BLOOD", "T1-MARROW", "T1-SOUL", "CIRC",
               "MER-PART", "MER-FULL", "MER-NET", "XT-FIELD", "CORE-ON", "DIVINE"]
CULT_LINKS = ["DUAL-STREAM", "LINK-PRIOR", "LINK-STEP", "LINK-GUARD", "LAW-INSIGHT"]
AFFINITY_CODES = ["NONE", "A2", "A3", "A4", "A5", "A6", "A7"]
SOV_CODES = ["NONE", "SOV-C", "SOV-CW", "SOV-H", "SOV-O"]
AFFINITY_LEVELS = {"Null": 1, "Whisper": 2, "Echo": 3, "Resonance": 4, "Attunement": 5, "Harmony": 6,
                   "Communion": 7, "Sovereignty": 8, "Origin Convergence": 9}

ORIGINS = ["Common", "Azorion", "Gale", "Brackenhold", "Personal", "Olympus", "Found"]
STATUSES = ["Active", "Dormant", "Lost", "Superseded"]
CHANNELS_INST = ["LIB", "COL", "ACA", "SECT", "ORG", "KNG", "EMP"]
CHANNELS_FOUND = ["QST", "TMB", "VLT", "RLC", "MEN"]
ACCESS_CODES = ["OPEN", "ENROLLED", "MEMBER", "RANKED", "PERMIT", "SEALED"]
COPY_CODES = ["FREE", "LENDING", "RESTRICTED", "SEALED"]
MASTERY = ["Novice", "Practiced", "Adept", "Proficient", "Expert", "Master"]
FORMS = ["INSTANT", "CHANNELED", "CAST"]
COST_CLASSES = ["STAMINA", "MINIMAL", "LOW", "MODERATE", "HIGH", "VARIABLE", "VERY-HIGH", "EXTREME", "REALITY"]
COST_RANGE = {"Basic": ["STAMINA", "MINIMAL", "LOW"], "Intermediate": ["LOW", "MODERATE"],
              "Advanced": ["MODERATE", "HIGH"], "Elite": ["HIGH"], "Signature": ["VARIABLE"],
              "Fusion": ["VERY-HIGH"], "Catastrophic": ["EXTREME"], "Mythic": ["REALITY"]}
FORM_ALLOWED = {"Basic": ["INSTANT", "CHANNELED"], "Intermediate": ["INSTANT", "CHANNELED"],
                "Advanced": FORMS, "Elite": FORMS, "Signature": FORMS, "Fusion": FORMS,
                "Catastrophic": ["INSTANT", "CAST"], "Mythic": ["INSTANT", "CAST"]}
FUNCTIONS = {"Attack": ["Strike", "Projectile", "Area", "Penetrating", "TrueDamage", "Suppression"],
             "Defense": ["Shield", "Deflect", "Absorb", "Reflect", "Nullify"],
             "Mobility": ["Step", "Flash", "Phase"],
             "Control": ["Bind", "Seal", "Suppress", "Disrupt", "Confuse"],
             "Trap": ["Trap", "Formation", "Contaminate"],
             "Support": ["Heal", "Empower", "Sense"],
             "Combination": ["Sequence", "Convergence"]}
INSTITUTIONS = ["Nine Halls", "Sapphire Ascent Academy", "Lyraen Heights Academy", "Windward Reach Academy",
                "Azure Crafters Concord", "Skysworn", "Azure Guard", "Stormbreak Academy", "Aerie Academy",
                "Long Coast Academy", "Oath-Voices", "Stormwing Order", "Windward Host", "Long Coast Fleet",
                "Wind-Sworn Militia", "Aerie Artificers College", "Long Coast Shipwrights Order"]
FIREARMS = {"PST", "MUS", "RIF", "SHG", "CAN", "GRN"}  # Gale firearms exception (ledger-manuals ruling 10)
SWORD_FAMILIES = {"Bladed swords"}
SWORD_CODES_EXTRA = {"HKS", "BFS"}
UNARMED_FAMILY = "Unarmed and close aids"

# ---- Cultivation axis (Canon Amendment 2026-10-16; _design-cultivation-axis.md sections 2 to 11) -------------------
AXIS_DIR = "cultivation"
H_CAFF = ("affinity_id,domain,name,description,prominence,basic_n,inter_n,adv_n,adv_common_n,adv_kingdom_n,elite_n,sig_n,"
          "fus_n,cat_n,myt_n,req_kind,support_role")
H_CMANUALS = H_MANUALS.replace("weapon_id", "affinity_id")
H_CMOVES = H_MOVES.replace("manual_id,seq", "manual_id,affinity_id,seq")
H_CKINGDOM = H_KINGDOM
H_CPERSONAL = H_PERSONAL.replace("weapon_id", "affinity_id")
H_CKITS = H_KITS
H_CCHARS = "char_id,soul_rung,soul_types,heart_level,healer"
# code:class:req_kind for the 65 disciplines (design section 2). P Prominent, S Standard, N Niche, R Rare.
_AFF_TEXT = ("EAR:P:A FIR:P:A WAT:P:A WND:P:A THN:P:A MTL:P:A WOD:P:A SWD:P:A STR:P:A ICE:S:A PSN:S:A SND:S:A SVB:S:A "
             "CRY:N:A MGM:N:A LGT:S:A DRK:S:A SUN:S:A SPC:S:A GRV:N:A CEL:N:A MOO:N:A TIM:R:A LIF:P:A DTH:S:A BLD:S:A "
             "BON:N:A SLA:N:A RNC:R:A STM:S:A MST:N:A ILL:S:A WIL:S:A CHS:S:A ORD:S:A DRM:N:A MEM:N:A TAO:R:A FAT:R:A "
             "KRM:R:A TRU:R:A VOD:R:A HEA:P:A PRT:P:A SEA:S:A BND:S:A CRE:R:A DST:R:A INF:R:A BAL:R:A SOW:S:SR SOD:S:SR "
             "SOS:S:SR SOH:S:SR SOT:N:SR SOC:N:SR SOP:N:SR SOB:N:SR SOR:N:SR SON:N:SR SOV:R:SR BDY:P:NONE QIP:P:NONE "
             "HRT:S:HL FRM:N:NONE")
AFF_CLASS = {}
AFF_KIND = {}
for _tok in _AFF_TEXT.split():
    _c, _p, _k = _tok.split(":")
    AFF_CLASS[_c] = {"P": "Prominent", "S": "Standard", "N": "Niche", "R": "Rare"}[_p]
    AFF_KIND[_c] = _k
AFF_CODES = list(AFF_CLASS)
# design section 6: class -> (basic, inter, adv_common, adv_kingdom, elite, sig, fus, cat, myt); elite and sig per kingdom
CLASS_COUNTS = {"Prominent": (10, 8, 4, 3, 6, 5, 4, 3, 2), "Standard": (8, 7, 3, 3, 5, 4, 3, 2, 1),
                "Niche": (6, 5, 2, 2, 4, 3, 2, 1, 1), "Rare": (4, 4, 2, 2, 3, 2, 2, 2, 2)}
SR_CODES = [f"SR{i}" for i in range(1, 13)]
HL_CODES = [f"HL{i}" for i in range(1, 6)]
FUNCTIONS_C = {k: list(v) for k, v in FUNCTIONS.items()}
FUNCTIONS_C["Support"] = FUNCTIONS_C["Support"] + ["Revive", "Cleanse"]
# C-29 support roles (design section 7): primary needs >= 50 percent Support moves, secondary >= 15 percent
SUPPORT_PRIMARY = {"HEA": "heal", "LIF": "heal", "SOH": "heal", "SOS": "sense", "SOR": "empower"}
SUPPORT_SECONDARY = {"PRT", "WAT", "WOD", "SUN", "LGT", "BLD", "RNC", "DTH", "TIM", "CRE", "BAL", "WIL", "ORD", "STR",
                     "HRT", "SPC", "TRU", "WND", "SVB", "QIP", "BDY"}
SECONDARY_ONLY = {"DTH": {"Cleanse"}}  # DTH counts Cleanse moves only
HEALING_FUNCS = {"Heal", "Revive", "Cleanse"}
# cultivation windows (design section 5): every manual opens at Warrior or above; no M1 band
CWINDOWS = {k: v for k, v in WINDOWS.items() if k[1] != "M1"}
CWINDOWS.update({
    ("BAS", "M2"): [("Warrior L1 Low", "Warrior L9 Peak")],
    ("INT", "M2"): [("Warrior L1 Low", "Champion L9 Peak")],
    ("SIG", "M2"): [("Warrior L1 Low", "Ruler L1 Mid")],
})
# soul-type disciplines (OPEN-1, Part 4 Area 2.2): XT from Demigod, no M2 window except the Early Awakening Basic at Monarch
CWINDOWS_SR = {k: v for k, v in CWINDOWS.items() if k[1] != "M2"}
CWINDOWS_SR[("BAS", "XT")] = [("Demigod L1 Low", "Void God L9 Peak")]
CWINDOWS_SR[("INT", "XT")] = [("Demigod L1 Low", "Void God L9 Peak")]
EARLY_AWAKENING = ("Monarch L1 Low", "Monarch L9 Peak")  # BAS in band M2 for an SR discipline
CFLOOR = "Warrior L1 Low"
A_BAND_CAP = {"M2": 3, "XT": 5, "CF": 6, "DV": 7}
# Part 42 Area 6 Fusion rows: band -> (cultivation_req, sovereignty_req); energy QI-VHI, affinity A4+A4
FUSION_REQ = {"XT": ("DUAL-STREAM+XT-FIELD+LINK-PRIOR", "NONE"), "CF": ("DUAL-STREAM+CORE-ON+LINK-PRIOR", "SOV-C")}

RE_REALM = re.compile(r"^(?P<realm>[A-Za-z ]+?) L(?P<n>[1-9]) (?P<sub>Low|Mid|High|Peak)$")
RE_T1 = re.compile(r"^T1 (?P<stage>[A-Za-z]+)$")
RE_MAN = re.compile(r"^MAN-(?P<g>[A-Z]{3})-(?P<w>[A-Z]{3})-(?P<n>\d{3})$")
RE_MV = re.compile(r"^MV-(?P<g>[A-Z]{3})-(?P<w>[A-Z]{3})-(?P<n>\d{3})-(?P<s>\d{2})$")
RE_KING = re.compile(r"^(?P<k>AZ|GA|BR)-(?P<g>[A-Z]{3})-(?P<w>[A-Z]{3})-(?P<n>\d{3})$")
RE_PER = re.compile(r"^PER-(?P<c>[A-Z]{3})-(?P<n>\d{2})$")
RE_PERMV = re.compile(r"^PER-(?P<c>[A-Z]{3})-(?P<n>\d{2})-(?P<s>\d{2})$")
RE_FND = re.compile(r"^FND-(?P<n>\d{3})$")
RE_FNDMV = re.compile(r"^FND-(?P<n>\d{3})-(?P<s>\d{2})$")
RE_FIRST_AREA = re.compile(r"^(Area \d+|Chapter \d{3}) — .+ \(Ref: [0-9.]+\)$")
RE_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_FUNCTION = re.compile(r"^(Soul-)?(?P<c>[A-Za-z]+):(?P<s>[A-Za-z]+)$")
RE_UNDERSCORE_MARK = re.compile(r"(^|[^\w])_[^_\s][^_]*_([^\w]|$)")
RE_CHR = re.compile(r"^[A-Z]{3}$")
RE_CMAN = re.compile(r"^CMAN-(?P<g>[A-Z]{3})-(?P<w>[A-Z]{3})-(?P<n>\d{3})$")
RE_CMV = re.compile(r"^CMV-(?P<g>[A-Z]{3})-(?P<w>[A-Z]{3})-(?P<n>\d{3})-(?P<s>\d{2})$")
RE_CKING = re.compile(r"^(?P<k>CAZ|CGA)-(?P<g>[A-Z]{3})-(?P<w>[A-Z]{3})-(?P<n>\d{3})$")
RE_PCM = re.compile(r"^PCM-(?P<c>[A-Z]{3})-(?P<n>\d{2})$")
RE_PCMMV = re.compile(r"^PCM-(?P<c>[A-Z]{3})-(?P<n>\d{2})-(?P<s>\d{2})$")
DEFAULT_FIRST_AREA = "Not yet established"
EM_DASH = "—"


# ---------------------------------------------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------------------------------------------

def realm_pos(s):
    """Parse a min_realm / effective_realm string into a comparable tuple, or None when malformed."""
    s = (s or "").strip()
    m = RE_T1.match(s)
    if m:
        if m.group("stage") not in T1_STAGES:
            return None
        return (0, T1_STAGES.index(m.group("stage")), 0)
    m = RE_REALM.match(s)
    if not m or m.group("realm") not in REALM_INDEX or m.group("realm") == "T1":
        return None
    return (REALM_INDEX[m.group("realm")], int(m.group("n")), ["Low", "Mid", "High", "Peak"].index(m.group("sub")))


def realm_name(s):
    s = (s or "").strip()
    if RE_T1.match(s):
        return "T1"
    m = RE_REALM.match(s)
    return m.group("realm") if m else None


def realm_band(s):
    n = realm_name(s)
    if n is None:
        return None
    i = REALM_INDEX[n]
    if i == 0:
        return "M1"
    if i <= 5:
        return "M2"
    if i <= 9:
        return "XT"
    if i <= 12:
        return "CF"
    return "DV"


def access_group(s):
    n = realm_name(s)
    return REALM_TO_AG.get(n) if n else None


def compare_form(text):
    t = "".join(ch if (ch.isalnum() or ch.isspace()) else " " for ch in (text or "").lower().replace("'", ""))
    return " ".join(t.split())


def parse_comp(cell):
    out = {}
    for tok in (cell or "").split():
        m = re.fullmatch(r"([BIAESFCM])(\d+)", tok)
        if not m:
            return None
        out[LETTER_TYPE[m.group(1)]] = int(m.group(2))
    return out


def split_codes(cell, sep=";"):
    cell = (cell or "").strip()
    if cell == "" or cell.lower() == "none":
        return []
    return [c.strip() for c in cell.split(sep) if c.strip()]


class IdInfo:
    axis = "weapon"

    def __init__(self, kind, rel_file, **kw):
        self.kind = kind          # manual, move, kingdom, personal, personal_move, found, found_move
        self.rel_file = rel_file  # path relative to root
        self.__dict__.update(kw)


def parse_id(i):
    """Turn an ID into its kind and the one file that names it (Rule 42.10.1.2). None when it matches no scheme."""
    i = (i or "").strip()
    ci = parse_cult_id(i)
    if ci is not None:
        return ci
    m = RE_MAN.match(i)
    if m and m.group("g") in CODE_TO_FOLDER:
        return IdInfo("manual", f"manuals/{CODE_TO_FOLDER[m['g']]}/{m['w']}.csv", grade=m["g"], wpn=m["w"], nnn=m["n"])
    m = RE_MV.match(i)
    if m and m.group("g") in CODE_TO_FOLDER:
        return IdInfo("move", f"moves/{CODE_TO_FOLDER[m['g']]}/{m['w']}.csv", grade=m["g"], wpn=m["w"], nnn=m["n"],
                      seq=m["s"], manual_id=f"MAN-{m['g']}-{m['w']}-{m['n']}")
    m = RE_KING.match(i)
    if m and m.group("g") in CODE_TO_FOLDER:
        f = {"AZ": "azorion", "GA": "gale", "BR": "brackenhold"}[m["k"]]
        return IdInfo("kingdom", f"kingdoms/{f}.csv", grade=m["g"], wpn=m["w"], nnn=m["n"], king=m["k"],
                      manual_id=f"MAN-{m['g']}-{m['w']}-{m['n']}")
    m = RE_PER.match(i)
    if m:
        return IdInfo("personal", f"personal/{m['c'].lower()}-manuals.csv", chr=m["c"], nn=m["n"])
    m = RE_PERMV.match(i)
    if m:
        return IdInfo("personal_move", f"personal/{m['c'].lower()}-moves.csv", chr=m["c"], nn=m["n"], seq=m["s"],
                      manual_id=f"PER-{m['c']}-{m['n']}")
    m = RE_FND.match(i)
    if m:
        return IdInfo("found", "found/found-manuals.csv", nnn=m["n"])
    m = RE_FNDMV.match(i)
    if m:
        return IdInfo("found_move", "found/found-moves.csv", nnn=m["n"], seq=m["s"], manual_id=f"FND-{m['n']}")
    return None


def parse_cult_id(i):
    """Cultivation-axis IDs (CMAN-, CMV-, CAZ-/CGA-, PCM-); same kinds as the weapon axis, axis = 'cultivation'."""
    d = AXIS_DIR + "/"
    m = RE_CMAN.match(i)
    if m and m.group("g") in CODE_TO_FOLDER:
        return IdInfo("manual", f"{d}manuals/{CODE_TO_FOLDER[m['g']]}/{m['w']}.csv", axis="cultivation", grade=m["g"],
                      wpn=m["w"], nnn=m["n"])
    m = RE_CMV.match(i)
    if m and m.group("g") in CODE_TO_FOLDER:
        return IdInfo("move", f"{d}moves/{CODE_TO_FOLDER[m['g']]}/{m['w']}.csv", axis="cultivation", grade=m["g"],
                      wpn=m["w"], nnn=m["n"], seq=m["s"], manual_id=f"CMAN-{m['g']}-{m['w']}-{m['n']}")
    m = RE_CKING.match(i)
    if m and m.group("g") in CODE_TO_FOLDER:
        f = {"CAZ": "azorion", "CGA": "gale"}[m["k"]]
        return IdInfo("kingdom", f"{d}kingdoms/{f}.csv", axis="cultivation", grade=m["g"], wpn=m["w"], nnn=m["n"],
                      king=m["k"], manual_id=f"CMAN-{m['g']}-{m['w']}-{m['n']}")
    m = RE_PCM.match(i)
    if m:
        return IdInfo("personal", f"{d}personal/{m['c'].lower()}-manuals.csv", axis="cultivation", chr=m["c"], nn=m["n"])
    m = RE_PCMMV.match(i)
    if m:
        return IdInfo("personal_move", f"{d}personal/{m['c'].lower()}-moves.csv", axis="cultivation", chr=m["c"],
                      nn=m["n"], seq=m["s"], manual_id=f"PCM-{m['c']}-{m['n']}")
    return None


def manual_moves_file(info):
    """The moves file that carries the moves of a manual (generic, personal or found)."""
    if info.axis == "cultivation":
        if info.kind == "manual":
            return f"{AXIS_DIR}/moves/{CODE_TO_FOLDER[info.grade]}/{info.wpn}.csv"
        if info.kind == "personal":
            return f"{AXIS_DIR}/personal/{info.chr.lower()}-moves.csv"
        return None
    if info.kind == "manual":
        return f"moves/{CODE_TO_FOLDER[info.grade]}/{info.wpn}.csv"
    if info.kind == "personal":
        return f"personal/{info.chr.lower()}-moves.csv"
    if info.kind == "found":
        return "found/found-moves.csv"
    return None


# ---------------------------------------------------------------------------------------------------------------
# Reading CSV files (read-only)
# ---------------------------------------------------------------------------------------------------------------

class Table:
    def __init__(self, rel):
        self.rel = rel
        self.exists = False
        self.header = []
        self.rows = []        # list of dicts, each with "_line" (1-based file line) and "_file"
        self.format_problems = []  # (line, message)
        self.bad_header = False


def read_table(root, rel, canonical=None):
    """Read one CSV into a Table. Never raises on missing files. Records format problems; writes nothing."""
    t = Table(rel)
    path = root / rel
    if not path.is_file():
        return t
    t.exists = True
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        t.format_problems.append((1, "file starts with a byte-order mark"))
        raw = raw[3:]
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        t.format_problems.append((1, f"not valid UTF-8 ({e.reason} at byte {e.start})"))
        text = raw.decode("utf-8", errors="replace")
    if text == "":
        t.format_problems.append((1, "empty file (no header row)"))
        t.bad_header = True
        return t
    if not text.endswith("\n"):
        t.format_problems.append((text.count("\n") + 1, "file does not end with a line break"))
    elif text.endswith("\n\n") or text.endswith("\r\n\r\n"):
        t.format_problems.append((text.count("\n"), "file ends with a blank line"))
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    first = True
    for idx, line in enumerate(lines, start=1):
        line = line.rstrip("\r")
        if line.strip() == "":
            if not (first is False and idx == len(lines)):
                t.format_problems.append((idx, "blank line"))
            continue
        try:
            cells = next(csv.reader([line], strict=True))
        except csv.Error as e:
            t.format_problems.append((idx, f"unreadable CSV record ({e}); a cell may hold a line break or a stray quote"))
            continue
        if first:
            first = False
            t.header = cells
            if canonical is not None and ",".join(cells) != canonical:
                t.bad_header = True
            continue
        if len(cells) != len(t.header):
            t.format_problems.append((idx, f"{len(cells)} cells, header has {len(t.header)}"))
            continue
        d = dict(zip(t.header, cells))
        d["_line"] = idx
        d["_file"] = rel
        t.rows.append(d)
    return t


def lookup_rows(root, rel, key, value):
    t = read_table(root, rel)
    return t, [r for r in t.rows if r.get(key) == value]


# ---------------------------------------------------------------------------------------------------------------
# Whole-ledger loader used by validate, stats, find-name
# ---------------------------------------------------------------------------------------------------------------

class Ledger:
    def __init__(self, root):
        self.root = root
        self.tables = {}
        self.weapons = {}       # code -> row
        self.weapon_order = []
        self.manuals = {}       # manual_id -> row (generic, personal, found)
        self.moves_by_manual = {}   # manual_id -> [move rows]
        self.moves = {}         # move_id -> row
        self.kingdom_rows = {}  # kingdom_id -> row
        self.chars = {}
        self.kits = []
        self.missing = {"manuals": [], "moves": [], "header-only manuals": [], "header-only moves": [],
                        "kingdoms": [], "characters": False, "character-kits": False}
        self.loaded_files = []
        self.load()

    def table(self, rel, canonical):
        t = read_table(self.root, rel, canonical)
        self.tables[rel] = t
        if t.exists:
            self.loaded_files.append(rel)
        return t

    def load(self):
        wt = self.table("weapons.csv", H_WEAPONS)
        if wt.exists and not wt.bad_header:
            for r in wt.rows:
                if r["weapon_id"] not in self.weapons:
                    self.weapons[r["weapon_id"]] = r
                    self.weapon_order.append(r["weapon_id"])
        for g in GRADE_CODES:
            folder = CODE_TO_FOLDER[g]
            for w in self.weapon_order:
                for kind, hdr in (("manuals", H_MANUALS), ("moves", H_MOVES)):
                    rel = f"{kind}/{folder}/{w}.csv"
                    t = self.table(rel, hdr)
                    if not t.exists:
                        key = kind if g in STOCK_GRADES else f"header-only {kind}"
                        self.missing[key].append(rel)
        # stray files in grade folders (not named by a weapon code) are loaded too so they are validated
        for kind, hdr in (("manuals", H_MANUALS), ("moves", H_MOVES)):
            for folder in GRADE_FOLDERS:
                d = self.root / kind / folder
                if d.is_dir():
                    for p in sorted(d.glob("*.csv")):
                        rel = f"{kind}/{folder}/{p.name}"
                        if rel not in self.tables:
                            self.table(rel, hdr)
        for k in ("azorion", "gale", "brackenhold"):
            t = self.table(f"kingdoms/{k}.csv", H_KINGDOM)
            if not t.exists and k != "brackenhold":  # Brackenhold file is loaded when present (Canon Amendment 2026-10-08)
                self.missing["kingdoms"].append(f"kingdoms/{k}.csv")
        pdir = self.root / "personal"
        if pdir.is_dir():
            for p in sorted(pdir.glob("*-manuals.csv")):
                self.table(f"personal/{p.name}", H_PERSONAL)
            for p in sorted(pdir.glob("*-moves.csv")):
                self.table(f"personal/{p.name}", H_MOVES)
        fdir = self.root / "found"
        if fdir.is_dir():
            self.table("found/found-manuals.csv", H_PERSONAL)
            self.table("found/found-moves.csv", H_MOVES)
        ct = self.table("characters.csv", H_CHARS)
        self.missing["characters"] = not ct.exists
        kt = self.table("character-kits.csv", H_KITS)
        self.missing["character-kits"] = not kt.exists
        # indexes (first occurrence wins; duplicates are reported by validate)
        for rel, t in self.tables.items():
            if t.bad_header:
                continue
            if rel.startswith("manuals/") or (rel.startswith("personal/") and rel.endswith("-manuals.csv")) \
                    or rel == "found/found-manuals.csv":
                for r in t.rows:
                    self.manuals.setdefault(r["manual_id"], r)
            elif rel.startswith("moves/") or (rel.startswith("personal/") and rel.endswith("-moves.csv")) \
                    or rel == "found/found-moves.csv":
                for r in t.rows:
                    self.moves.setdefault(r["move_id"], r)
                    self.moves_by_manual.setdefault(r["manual_id"], []).append(r)
            elif rel.startswith("kingdoms/"):
                for r in t.rows:
                    self.kingdom_rows.setdefault(r["kingdom_id"], r)
        if ct.exists and not ct.bad_header:
            for r in ct.rows:
                self.chars.setdefault(r["char_id"], r)
        if kt.exists and not kt.bad_header:
            self.kits = kt.rows

    def sorted_moves(self, mid):
        return sorted(self.moves_by_manual.get(mid, []), key=lambda r: (r.get("seq", ""), r["_line"]))

    def file_exists(self, rel):
        t = self.tables.get(rel)
        return bool(t and t.exists)


# ---------------------------------------------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------------------------------------------

class Report:
    def __init__(self):
        self.items = []   # (sev, check, loc, msg)
        self.pending = {}
        self.cpend = {}   # cultivation-axis counts of files / rows not yet generated (INFO, never a problem)

    def fail(self, check, loc, msg):
        self.items.append(("FAIL", check, loc, msg))

    def info(self, check, loc, msg):
        self.items.append(("INFO", check, loc, msg))

    def pend(self, what, n=1):
        self.pending[what] = self.pending.get(what, 0) + n


def loc(r, id_=None):
    s = f"{r['_file']}:{r['_line']}"
    return s


def expected_rows(grade, w):
    def n(k):
        try:
            return int(w[k])
        except (KeyError, ValueError):
            return None
    parts = {"BAS": ("basic_n",), "INT": ("inter_n",), "ADV": ("adv_common_n", "adv_kingdom_n"),
             "ELI": ("elite_n",), "SIG": ("sig_n",)}.get(grade)
    if parts is None:
        return 0
    vals = [n(k) for k in parts]
    if None in vals:
        return None
    firearm = w.get("weapon_id") in FIREARMS  # Gale firearms exception (ruling 10): Azorion only above Common
    if grade == "ADV":
        return vals[0] + (1 if firearm else 2) * vals[1]
    if grade in ("ELI", "SIG"):
        return (1 if firearm else 2) * vals[0]
    return vals[0]


def bh_extra(L, grade, wcode):
    """Number of Brackenhold-origin manual rows of one grade and weapon (counted on top of weapons.csv)."""
    t = L.tables.get(f"manuals/{CODE_TO_FOLDER[grade]}/{wcode}.csv") if grade in CODE_TO_FOLDER else None
    if not t or not t.exists or t.bad_header:
        return 0
    return sum(1 for r in t.rows if r.get("origin") == "Brackenhold")


def expected_origin(grade, nnn, w):
    """The origin Rule 42.10.2.3 expects for number nnn (int) of a grade and weapon row w; None if unknown."""
    firearm = w.get("weapon_id") in FIREARMS
    try:
        total = expected_rows(grade, w)
        if total is not None and nnn > total:
            return "Brackenhold"  # extras after Gale (Canon Amendment 2026-10-08)
        if grade in ("BAS", "INT"):
            return "Common"
        if grade == "ADV":
            c, k = int(w["adv_common_n"]), int(w["adv_kingdom_n"])
            return "Common" if nnn <= c else ("Azorion" if (nnn <= c + k or firearm) else "Gale")
        if grade == "ELI":
            e = int(w["elite_n"])
            return "Azorion" if (nnn <= e or firearm) else "Gale"
        if grade == "SIG":
            return "Azorion" if (nnn <= 6 or firearm) else "Gale"
    except (KeyError, ValueError):
        return None
    return None


def check_unlock_floor(min_pos, moves):
    if not moves:
        return None
    lowest = min(moves, key=lambda m: TYPE_RANK.get(m["move_type"], 99))
    u = UNLOCK_REALM.get(lowest["move_type"])
    if u is None:
        return None
    if min_pos < realm_pos(u):
        return f"min_realm is below the unlock realm {u} of its lowest move type {lowest['move_type']}"
    return None


def validate(L, rep):
    root = L.root
    story_memory = root.parent if root.parent.name == "story-memory" else None

    # ---- weapons.csv --------------------------------------------------------------------------------------
    wt = L.tables.get("weapons.csv")
    if not wt or not wt.exists:
        rep.fail("C-1", "weapons.csv", "weapons.csv is missing (every count check depends on it)")
    # ---- C-1 format and header, per file ------------------------------------------------------------------
    for rel, t in L.tables.items():
        if not t.exists:
            continue
        if t.bad_header:
            if t.header:
                rep.fail("C-1", f"{rel}:1", "header line differs from the canonical header; file skipped by later checks")
        for line, msg in t.format_problems:
            rep.fail("C-1", f"{rel}:{line}", msg)
    if wt and wt.exists and not wt.bad_header:
        seen = {}
        for r in wt.rows:
            if r["weapon_id"] in seen:
                rep.fail("C-2", loc(r), f"duplicate weapon_id {r['weapon_id']} (first at line {seen[r['weapon_id']]})")
            seen.setdefault(r["weapon_id"], r["_line"])
            for k in ("basic_n", "inter_n", "adv_n", "adv_common_n", "adv_kingdom_n", "elite_n", "sig_n"):
                if not r[k].isdigit():
                    rep.fail("C-1", loc(r), f"{k} is not an integer: {r[k]!r}")

    # ---- C-14 plain text, every cell of every file ---------------------------------------------------------
    for rel, t in L.tables.items():
        if not t.exists or t.bad_header:
            continue
        for r in t.rows:
            for k in t.header:
                v = r.get(k, "")
                bad = []
                if "*" in v:
                    bad.append("asterisk")
                if "`" in v:
                    bad.append("backtick")
                if "\t" in v:
                    bad.append("tab")
                if RE_UNDERSCORE_MARK.search(v):
                    bad.append("underscore mark-up")
                if EM_DASH in v and k != "first_area":
                    bad.append("em dash")
                if bad:
                    rep.fail("C-14", loc(r), f"column {k} holds {', '.join(bad)}: {v[:50]!r}")

    # ---- manuals: C-2, C-4, C-6, C-7, C-9, C-10 (code lists), C-15, C-16, C-18 --------------------------------
    seen_ids = {}

    def dup(idv, r):
        key = idv
        if key in seen_ids:
            rep.fail("C-2", loc(r), f"duplicate ID {idv} (first at {seen_ids[key]})")
        else:
            seen_ids[key] = loc(r)

    manual_tables = [(rel, t) for rel, t in L.tables.items() if t.exists and not t.bad_header and (
        rel.startswith("manuals/") or (rel.startswith("personal/") and rel.endswith("-manuals.csv"))
        or rel == "found/found-manuals.csv")]
    move_tables = [(rel, t) for rel, t in L.tables.items() if t.exists and not t.bad_header and (
        rel.startswith("moves/") or (rel.startswith("personal/") and rel.endswith("-moves.csv"))
        or rel == "found/found-moves.csv")]

    # rows per generic file against weapons.csv
    counts_by_file = {}
    for rel, t in manual_tables:
        counts_by_file[rel] = len(t.rows)
        generic = rel.startswith("manuals/")
        parts = rel.split("/")
        fgrade = FOLDER_TO_CODE.get(parts[1]) if generic else None
        fwpn = parts[2][:-4] if generic else None
        pchar = None
        if rel.startswith("personal/"):
            pchar = parts[1].split("-")[0].upper()
        prev_nnn = 0
        for r in t.rows:
            mid = r["manual_id"]
            dup(mid, r)
            info = parse_id(mid)
            if generic:
                if not info or info.kind != "manual":
                    rep.fail("C-2", loc(r), f"manual_id {mid!r} is not a MAN-GRD-WPN-NNN ID")
                else:
                    if info.rel_file != rel:
                        rep.fail("C-2", loc(r), f"{mid} belongs in {info.rel_file}")
                    if r["grade"] != info.grade:
                        rep.fail("C-2", loc(r), f"{mid}: grade cell {r['grade']!r} differs from ID grade {info.grade}")
                    if r["weapon_id"] != info.wpn:
                        rep.fail("C-15", loc(r), f"{mid}: weapon_id {r['weapon_id']!r} differs from ID weapon {info.wpn}")
                    # C-4 numbering
                    n = int(info.nnn)
                    if n != prev_nnn + 1:
                        rep.fail("C-4", loc(r), f"{mid}: number {info.nnn} is not contiguous (expected {prev_nnn + 1:03d})")
                    prev_nnn = n
                    w = L.weapons.get(info.wpn)
                    if w:
                        eo = expected_origin(info.grade, n, w)
                        if eo and r["origin"] != eo:
                            rep.fail("C-4", loc(r), f"{mid}: origin {r['origin']!r}, number order expects {eo}")
                        er = expected_rows(info.grade, w)
                        if er is not None:
                            er += bh_extra(L, info.grade, info.wpn)
                        if er is not None and n > er:
                            rep.fail("C-3", loc(r), f"{mid}: number {n} is beyond the {er} rows weapons.csv gives {info.wpn} {info.grade}")
                    if r["origin"] not in ("Common", "Azorion", "Gale", "Brackenhold"):
                        rep.fail("C-2", loc(r), f"{mid}: generic manual origin {r['origin']!r} must be Common, Azorion, Gale or Brackenhold")
            else:
                kind_ok = (info and info.kind in ("personal", "found"))
                if not kind_ok:
                    rep.fail("C-18", loc(r), f"manual_id {mid!r} is not a PER-CHR-NN or FND-NNN ID")
                elif info.kind == "personal":
                    if info.chr != pchar:
                        rep.fail("C-18", loc(r), f"{mid}: character code {info.chr} differs from the file's {pchar}")
                    if r["owner"] != info.chr:
                        rep.fail("C-18", loc(r), f"{mid}: owner {r['owner']!r} differs from ID character {info.chr}")
                    n = int(info.nn)
                    if n != prev_nnn + 1:
                        rep.fail("C-4", loc(r), f"{mid}: number {info.nn} is not contiguous (expected {prev_nnn + 1:02d})")
                    prev_nnn = n
                    if L.chars and r["owner"] not in L.chars:
                        rep.fail("C-18", loc(r), f"{mid}: owner {r['owner']!r} is not in characters.csv")
                    if r["origin"] not in ("Personal", "Olympus"):
                        rep.fail("C-18", loc(r), f"{mid}: personal origin {r['origin']!r} must be Personal or Olympus")
                    src = r.get("source", "")
                    if src.split(":", 1)[0] not in CHANNELS_INST + CHANNELS_FOUND:
                        rep.fail("C-18", loc(r), f"{mid}: source {src!r} does not start with a channel code")
                if r.get("grade") not in GRADE_CODES:
                    rep.fail("C-2", loc(r), f"{mid}: grade {r.get('grade')!r} is not one of {' '.join(GRADE_CODES)}")
                if r.get("weapon_id") not in L.weapons and L.weapons:
                    rep.fail("C-15", loc(r), f"{mid}: weapon_id {r.get('weapon_id')!r} is not in weapons.csv")
            grade = r["grade"]
            # status, first_area (C-16)
            if r["status"] not in STATUSES:
                rep.fail("C-16", loc(r), f"{mid}: status {r['status']!r} not in {STATUSES}")
            fa = r["first_area"]
            if fa != DEFAULT_FIRST_AREA and not RE_FIRST_AREA.match(fa):
                rep.fail("C-16", loc(r), f"{mid}: first_area {fa!r} is neither 'Not yet established' nor the Area form")
            if r["origin"] not in ORIGINS:
                rep.fail("C-2", loc(r), f"{mid}: origin {r['origin']!r} not in {ORIGINS}")
            # weapon exists (generic: also checked by ID)
            if generic and L.weapons and r["weapon_id"] not in L.weapons:
                rep.fail("C-15", loc(r), f"{mid}: weapon_id {r['weapon_id']!r} is not in weapons.csv")
            # C-9 realm
            band = r["realm_band"]
            mp = realm_pos(r["min_realm"])
            if band not in BANDS:
                rep.fail("C-9", loc(r), f"{mid}: realm_band {band!r} not in {BANDS}")
            if mp is None:
                rep.fail("C-9", loc(r), f"{mid}: min_realm {r['min_realm']!r} is not 'T1 <Stage>' or '<Realm> L<n> <Low|Mid|High|Peak>'")
            else:
                rb = realm_band(r["min_realm"])
                if band in BANDS and rb != band:
                    rep.fail("C-9", loc(r), f"{mid}: min_realm {r['min_realm']} is in band {rb}, realm_band says {band}")
                win = WINDOWS.get((grade, band)) if grade in GRADE_CODES else None
                if win:
                    if not any(realm_pos(lo) <= mp <= realm_pos(hi) for lo, hi in win):
                        rep.fail("C-9", loc(r), f"{mid}: min_realm {r['min_realm']} is outside the window "
                                 f"{win[0][0]} to {win[0][1]} for {grade} {band}")
                elif band in BANDS and grade in GRADE_CODES:
                    rep.fail("C-9", loc(r), f"{mid}: no window exists for grade {grade} in band {band}")
                low_err = check_unlock_floor(mp, L.moves_by_manual.get(mid, []))
                if low_err:
                    rep.fail("C-9", loc(r), f"{mid}: {low_err}")
            # C-10 code lists
            e, c, a, s = r["energy_req"], r["cultivation_req"], r["affinity_req"], r["sovereignty_req"]
            if e not in ENERGY_LADDER:
                rep.fail("C-10", loc(r), f"{mid}: energy_req {e!r} not in the ladder")
            cparts = c.split("+")
            if cparts[0] not in CULT_STATES:
                rep.fail("C-10", loc(r), f"{mid}: cultivation_req state {cparts[0]!r} not in the state codes")
            for lk in cparts[1:]:
                if lk not in CULT_LINKS:
                    rep.fail("C-10", loc(r), f"{mid}: cultivation_req link {lk!r} not in the link codes")
            abase = a[:-1] if a.endswith("W") and a != "NONE" else a
            if abase not in AFFINITY_CODES and a != "A4+A4":
                rep.fail("C-10", loc(r), f"{mid}: affinity_req {a!r} not in the ladder")
            if s not in SOV_CODES:
                rep.fail("C-10", loc(r), f"{mid}: sovereignty_req {s!r} not in the ladder")
            if band == "M1" and (e != "NONE" or a != "NONE" or s != "NONE"):
                rep.fail("C-10", loc(r), f"{mid}: an M1 manual must have NONE in energy, affinity and sovereignty")
            if grade in GRADE_CODES and r["tradition"].strip() == "":
                rep.fail("C-1", loc(r), f"{mid}: tradition is empty")
            if r["title"].strip() == "":
                rep.fail("C-13", loc(r), f"{mid}: title is empty")
            # C-6 / C-7 count and composition
            mc = r["move_count"]
            if not mc.isdigit():
                rep.fail("C-6", loc(r), f"{mid}: move_count {mc!r} is not an integer")
                continue
            mcn = int(mc)
            if not 5 <= mcn <= 15:
                rep.fail("C-6", loc(r), f"{mid}: move_count {mcn} is outside 5 to 15")
            if grade in COUNT_RANGE and 5 <= mcn <= 15:
                lo, hi = COUNT_RANGE[grade]
                if not lo <= mcn <= hi:
                    rep.fail("C-7", loc(r), f"{mid}: move_count {mcn} is outside the {grade} range {lo} to {hi}")
                if grade == "CAT" and not generic and mcn not in (14, 15):
                    rep.fail("C-7", loc(r), f"{mid}: a personal Catastrophic manual has 14 or 15 moves, not {mcn}")
                tbl = COMPOSITION.get((grade, mcn))
                if r["composition"] != tbl:
                    rep.fail("C-6", loc(r), f"{mid}: composition {r['composition']!r} differs from the Part 42 table cell {tbl!r} for {grade} N={mcn}")
                pc = parse_comp(r["composition"])
                moves = L.moves_by_manual.get(mid)
                if moves is None:
                    mrel = manual_moves_file(info) if info else None
                    if mrel and not L.file_exists(mrel):
                        rep.pend("manuals whose moves file is not yet generated")
                    else:
                        rep.fail("C-15", loc(r), f"{mid}: no move rows exist for this manual")
                else:
                    if len(moves) != mcn:
                        rep.fail("C-6", loc(r), f"{mid}: move_count {mcn} but {len(moves)} move rows exist")
                    actual = {}
                    for mv in moves:
                        actual[mv["move_type"]] = actual.get(mv["move_type"], 0) + 1
                    if pc is not None and actual != pc:
                        rep.fail("C-6", loc(r), f"{mid}: move_type counts {fmt_comp(actual)} differ from composition {r['composition']!r}")
            # C-17 institutions are on kingdom rows (below)
    # C-3 row counts per weapon and grade
    for g in GRADE_CODES:
        folder = CODE_TO_FOLDER[g]
        for wcode in L.weapon_order:
            rel = f"manuals/{folder}/{wcode}.csv"
            t = L.tables.get(rel)
            exp = expected_rows(g, L.weapons[wcode])
            if exp is None:
                rep.fail("C-3", "weapons.csv", f"{wcode}: count columns for {g} are not integers")
                continue
            exp += bh_extra(L, g, wcode)  # Brackenhold-origin extras (Canon Amendment 2026-10-08)
            if not t or not t.exists:
                if exp:
                    rep.pend(f"manual files ({g}) not yet generated")
                continue
            if t.bad_header:
                continue
            got = len(t.rows)
            if got == exp:
                continue
            if got == 0 and exp > 0:
                rep.pend(f"manual files ({g}) present but header-only (not yet generated)")
            else:
                rep.fail("C-3", rel, f"{wcode} {g}: {got} manual rows, weapons.csv gives {exp}")

    # ---- moves: C-2, C-8, C-12, C-15, C-16 -----------------------------------------------------------------
    for rel, t in move_tables:
        generic = rel.startswith("moves/")
        parts = rel.split("/")
        for r in t.rows:
            mvid = r["move_id"]
            dup(mvid, r)
            info = parse_id(mvid)
            mid = r["manual_id"]
            minfo = parse_id(mid)
            if generic:
                if not info or info.kind != "move":
                    rep.fail("C-2", loc(r), f"move_id {mvid!r} is not a MV-GRD-WPN-NNN-SS ID")
                elif info.rel_file != rel:
                    rep.fail("C-2", loc(r), f"{mvid} belongs in {info.rel_file}")
            else:
                if not info or info.kind not in ("personal_move", "found_move"):
                    rep.fail("C-18", loc(r), f"move_id {mvid!r} is not a PER-CHR-NN-SS or FND-NNN-SS ID")
                elif info.kind == "personal_move" and info.chr != parts[1].split("-")[0].upper():
                    rep.fail("C-2", loc(r), f"{mvid} belongs in personal/{info.chr.lower()}-moves.csv")
            if info and info.manual_id != mid:
                rep.fail("C-8", loc(r), f"{mvid}: manual_id {mid!r} differs from the ID prefix {info.manual_id}")
            if info and r["seq"] != info.seq:
                rep.fail("C-8", loc(r), f"{mvid}: seq {r['seq']!r} differs from the ID suffix {info.seq}")
            if not re.fullmatch(r"\d{2}", r["seq"]):
                rep.fail("C-8", loc(r), f"{mvid}: seq {r['seq']!r} is not two digits")
            man = L.manuals.get(mid)
            if man is None:
                mrel = None
                if minfo:
                    mrel = minfo.rel_file
                if mrel and not L.file_exists(mrel):
                    rep.pend("move rows whose manuals file is not yet generated")
                else:
                    rep.fail("C-15", loc(r), f"{mvid}: manual_id {mid} has no manual row")
            mt = r["move_type"]
            if mt not in MOVE_TYPES:
                rep.fail("C-12", loc(r), f"{mvid}: move_type {mt!r} not in {MOVE_TYPES}")
                continue
            if man:
                comp = parse_comp(man["composition"])
                if comp is not None and mt not in comp:
                    rep.fail("C-8", loc(r), f"{mvid}: move_type {mt} is not in the manual's composition {man['composition']!r}")
                if man["grade"] in GRADE_PERCENTS and mt not in GRADE_PERCENTS[man["grade"]]:
                    rep.fail("C-8", loc(r), f"{mvid}: move_type {mt} is not a type of grade {man['grade']}")
            if r["name"].strip() == "":
                rep.fail("C-13", loc(r), f"{mvid}: name is empty")
            if r["status"] not in STATUSES:
                rep.fail("C-16", loc(r), f"{mvid}: status {r['status']!r} not in {STATUSES}")
            fa = r["first_area"]
            if fa != DEFAULT_FIRST_AREA and not RE_FIRST_AREA.match(fa):
                rep.fail("C-16", loc(r), f"{mvid}: first_area {fa!r} is neither 'Not yet established' nor the Area form")
            # C-12
            fn = r["function"]
            prim, _, sec = fn.partition("|")
            for part, label in ((prim, "primary"), (sec, "secondary")):
                if part == "" and label == "secondary" and "|" not in fn:
                    continue
                m = RE_FUNCTION.match(part)
                if not m or m.group("c") not in FUNCTIONS or m.group("s") not in FUNCTIONS[m.group("c")]:
                    rep.fail("C-12", loc(r), f"{mvid}: {label} function {part!r} is not a Part 6 Category:Sub")
                    continue
                sub, soul = m.group("s"), bool(m.group(1))
                rank = TYPE_RANK[mt]
                is_common = bool(man and man["origin"] == "Common")
                if (sub in ("Absorb", "Flash", "Phase", "TrueDamage", "Heal") or soul):
                    if rank < TYPE_RANK["Elite"]:
                        rep.fail("C-12", loc(r), f"{mvid}: function {part} appears only in Elite or above (move is {mt})")
                    if is_common:
                        rep.fail("C-12", loc(r), f"{mvid}: function {part} never appears in a Common manual")
                if sub == "Convergence" and mt != "Fusion":
                    rep.fail("C-12", loc(r), f"{mvid}: Convergence appears only in a Fusion-type move")
                if sub in ("Formation", "Trap") and rank < TYPE_RANK["Advanced"]:
                    rep.fail("C-12", loc(r), f"{mvid}: {sub} appears only in Advanced or above (move is {mt})")
            if r["form"] not in FORMS:
                rep.fail("C-12", loc(r), f"{mvid}: form {r['form']!r} not in {FORMS}")
            elif r["form"] not in FORM_ALLOWED[mt]:
                rep.fail("C-12", loc(r), f"{mvid}: a {mt} move may not take form {r['form']}")
            if r["cost_class"] not in COST_CLASSES:
                rep.fail("C-12", loc(r), f"{mvid}: cost_class {r['cost_class']!r} not in {COST_CLASSES}")
            elif r["cost_class"] not in COST_RANGE[mt]:
                rep.fail("C-12", loc(r), f"{mvid}: cost_class {r['cost_class']} is outside {COST_RANGE[mt]} for {mt}")
            if r["unlock_realm"] != UNLOCK_REALM[mt]:
                rep.fail("C-12", loc(r), f"{mvid}: unlock_realm {r['unlock_realm']!r} must be {UNLOCK_REALM[mt]!r} for {mt}")
            if mt == "Fusion" and not r["description"].startswith("streams:"):
                rep.fail("C-12", loc(r), f"{mvid}: a Fusion move's description must begin 'streams:'")
    # C-8 contiguity and order, per manual
    for mid, rows in L.moves_by_manual.items():
        rows_sorted = sorted(rows, key=lambda r: (r["seq"], r["_line"]))
        seqs = [r["seq"] for r in rows_sorted]
        want = [f"{i:02d}" for i in range(1, len(rows) + 1)]
        if seqs != want:
            rep.fail("C-8", f"{rows[0]['_file']}:{rows[0]['_line']}", f"{mid}: seq values {','.join(seqs)} are not contiguous 01..{len(rows):02d}")
        in_file = [r["seq"] for r in rows]
        if in_file != sorted(in_file):
            rep.fail("C-8", f"{rows[0]['_file']}:{rows[0]['_line']}", f"{mid}: move rows are not in seq order inside the file")
        ranks = [TYPE_RANK.get(r["move_type"], 0) for r in rows_sorted]
        if ranks != sorted(ranks):
            rep.fail("C-8", f"{rows[0]['_file']}:{rows[0]['_line']}", f"{mid}: moves do not run lowest type first")
    # C-15: every manual has at least one move row is covered in the manual loop (pending vs fail)

    # ---- C-11 Signature layout per kingdom and weapon ---------------------------------------------------------
    for wcode in L.weapon_order:
        t = L.tables.get(f"manuals/signature/{wcode}.csv")
        firearm = wcode in FIREARMS
        if not t or not t.exists or t.bad_header or len(t.rows) < (6 if firearm else 12):
            continue
        for base, kname in (((0, "Azorion"),) if firearm else ((0, "Azorion"), (6, "Gale"))):
            grp = t.rows[base:base + 6]
            bands = [r["realm_band"] for r in grp]
            if bands != ["M2", "M2", "M2", "M2", "XT", "CF"]:
                rep.fail("C-11", loc(grp[0]), f"{wcode} {kname} Signature bands are {bands}, expected M2 M2 M2 M2 XT CF")
            ps = [realm_pos(r["min_realm"]) for r in grp[:4]]
            if None not in ps:
                if ps != sorted(ps):
                    rep.fail("C-11", loc(grp[0]), f"{wcode} {kname} Signature M2 min_realm values are not non-decreasing")

    # ---- C-5 / C-17 kingdom rows ---------------------------------------------------------------------------
    def _strip_the(f):
        return f[4:] if f.startswith("the ") else f
    inst_forms = [_strip_the(compare_form(i)) for i in INSTITUTIONS]
    kingdom_by_manual = {"azorion": {}, "gale": {}, "brackenhold": {}}
    for kf, kname, pref in (("azorion", "Azure Sky", "AZ"), ("gale", "Gale", "GA"), ("brackenhold", "Brackenhold", "BR")):
        rel = f"kingdoms/{kf}.csv"
        t = L.tables.get(rel)
        if not t or not t.exists or t.bad_header:
            continue
        for r in t.rows:
            kid = r["kingdom_id"]
            dup(kid, r)
            info = parse_id(kid)
            if not info or info.kind != "kingdom":
                rep.fail("C-2", loc(r), f"kingdom_id {kid!r} is not an AZ-/GA-/BR- ID")
            else:
                if info.king != pref:
                    rep.fail("C-2", loc(r), f"{kid} belongs in the other kingdom file")
                if info.manual_id != r["manual_id"]:
                    rep.fail("C-2", loc(r), f"{kid}: manual_id {r['manual_id']} differs from the ID's {info.manual_id}")
            if r["kingdom"] != kname:
                rep.fail("C-5", loc(r), f"{kid}: kingdom {r['kingdom']!r} must be {kname!r} in this file")
            if r["channel"] not in CHANNELS_INST:
                rep.fail("C-5", loc(r), f"{kid}: channel {r['channel']!r} not in {CHANNELS_INST}")
            if r["access"] not in ACCESS_CODES:
                rep.fail("C-5", loc(r), f"{kid}: access {r['access']!r} not in {ACCESS_CODES}")
            if r["copy_control"] not in COPY_CODES:
                rep.fail("C-5", loc(r), f"{kid}: copy_control {r['copy_control']!r} not in {COPY_CODES}")
            if r["status"] not in STATUSES:
                rep.fail("C-16", loc(r), f"{kid}: status {r['status']!r} not in {STATUSES}")
            inst = r["institution"]
            if not inst.startswith("OPEN-AUTHOR"):
                f = compare_form(inst)
                f2 = _strip_the(f)
                if not any(f2 == i or i in f2 or f2 in i for i in inst_forms if f2):
                    rep.fail("C-17", loc(r), f"{kid}: institution {inst!r} is not in the Rule 42.7.2.2 list and does not begin OPEN-AUTHOR")
            man = L.manuals.get(r["manual_id"])
            if man is None:
                mi = parse_id(r["manual_id"])
                if mi and not L.file_exists(mi.rel_file):
                    rep.pend("kingdom rows whose manuals file is not yet generated")
                else:
                    rep.fail("C-15", loc(r), f"{kid}: manual_id {r['manual_id']} has no manual row")
            else:
                o = man["origin"]
                if kf == "gale" and o == "Common" and man["grade"] == "ADV" and man["weapon_id"] in FIREARMS:
                    rep.fail("C-5", loc(r), f"{kid}: Gale firearms exception: no Gale row for Common Advanced {man['weapon_id']} manual {r['manual_id']}")
                ok = (o == "Common") or (o == "Azorion" and kf == "azorion") or (o == "Gale" and kf == "gale")                     or (o == "Brackenhold" and kf == "brackenhold")
                if not ok:
                    rep.fail("C-5", loc(r), f"{kid}: a kingdom row never points at a manual of origin {o} ({r['manual_id']})")
            if r["manual_id"] in kingdom_by_manual[kf]:
                rep.fail("C-5", loc(r), f"{kid}: manual {r['manual_id']} already has a row in this kingdom file")
            kingdom_by_manual[kf][r["manual_id"]] = r
    # expected kingdom rows for each generic manual
    for mid, man in L.manuals.items():
        if not mid.startswith("MAN-"):
            continue
        o = man["origin"]
        need = [("azorion", "AZ")] if o == "Azorion" else [("gale", "GA")] if o == "Gale" else \
            [("brackenhold", "BR")] if o == "Brackenhold" else \
            [("azorion", "AZ"), ("gale", "GA")] if o == "Common" else []  # a Common manual's BR row is optional
        if o == "Common" and man["grade"] == "ADV" and man["weapon_id"] in FIREARMS:
            need = [("azorion", "AZ")]  # Gale firearms exception: no Gale row for Common Advanced firearm manuals
        for kf, pref in need:
            if not L.file_exists(f"kingdoms/{kf}.csv"):
                rep.pend(f"manuals awaiting a {kf} kingdom row (file not yet generated)")
            elif mid not in kingdom_by_manual[kf]:
                rep.fail("C-5", f"{man['_file']}:{man['_line']}", f"{mid} ({o}) has no row in kingdoms/{kf}.csv")

    # ---- C-13 names ------------------------------------------------------------------------------------------
    names = {}
    titles = {}
    for mid, man in L.manuals.items():
        titles.setdefault(compare_form(man["title"]), []).append(man)
    for mvid, mv in L.moves.items():
        names.setdefault(compare_form(mv["name"]), []).append(mv)
    for form, rows in names.items():
        if form and len(rows) > 1:
            for r in rows[1:]:
                rep.fail("C-13", loc(r), f"move name {r['name']!r} duplicates {rows[0]['move_id']} at {loc(rows[0])}")
    for form, rows in titles.items():
        if form and len(rows) > 1:
            for r in rows[1:]:
                rep.fail("C-13", loc(r), f"manual title {r['title']!r} duplicates {rows[0]['manual_id']} at {loc(rows[0])}")
    for form, rows in names.items():
        if form in titles:
            for r in rows:
                rep.fail("C-13", loc(r), f"move name {r['name']!r} equals manual title of {titles[form][0]['manual_id']}")
        if _strip_the(form) in inst_forms:
            for r in rows:
                rep.fail("C-13", loc(r), f"move name {r['name']!r} equals an institution name")
    for form, rows in titles.items():
        if _strip_the(form) in inst_forms:
            for r in rows:
                rep.fail("C-13", loc(r), f"manual title {r['title']!r} equals an institution name")

    # ---- C-19 characters ---------------------------------------------------------------------------------------
    ct = L.tables.get("characters.csv")
    if ct and ct.exists and not ct.bad_header:
        seen_c = {}
        for r in ct.rows:
            cid = r["char_id"]
            if not RE_CHR.match(cid):
                rep.fail("C-19", loc(r), f"char_id {cid!r} is not three capital letters")
            if cid in seen_c:
                rep.fail("C-19", loc(r), f"duplicate char_id {cid} (first at line {seen_c[cid]})")
            seen_c.setdefault(cid, r["_line"])
            if r["tier"] not in ("Hero", "A", "B", "C", "D"):
                rep.fail("C-19", loc(r), f"{cid}: tier {r['tier']!r} not in Hero A B C D")
            if r["kingdom"] not in ("Azure Sky", "Gale", "Brackenhold", "none"):
                rep.fail("C-19", loc(r), f"{cid}: kingdom {r['kingdom']!r} not in Azure Sky, Gale, Brackenhold, none")
            for k in ("realm", "effective_realm"):
                if r[k] != "OPEN-AUTHOR" and realm_pos(r[k]) is None:
                    rep.fail("C-19", loc(r), f"{cid}: {k} {r[k]!r} does not have the Rule 42.5.3.2 form")
            if realm_pos(r["realm"]) and realm_pos(r["effective_realm"]) and realm_pos(r["effective_realm"]) > realm_pos(r["realm"]):
                rep.fail("C-19", loc(r), f"{cid}: effective_realm is above the true realm")
            for b in split_codes(r["blocked_types"]):
                if b not in GRADE_CODES:
                    rep.fail("C-19", loc(r), f"{cid}: blocked_types code {b!r} is not a grade code")
            if r["blocked_types"].strip() == "":
                rep.fail("C-19", loc(r), f"{cid}: blocked_types is empty (use 'none')")
            for pw in split_codes(r["primary_weapons"]):
                if L.weapons and pw not in L.weapons:
                    rep.fail("C-19", loc(r), f"{cid}: primary_weapons code {pw!r} is not in weapons.csv")
            for aff in split_codes(r["affinity"]):
                if ":" not in aff or aff.split(":", 1)[1] not in AFFINITY_LEVELS:
                    rep.fail("C-19", loc(r), f"{cid}: affinity entry {aff!r} is not <Type>:<Part 4 level name>")
            sv = r["sovereignty"]
            if sv != "none" and not re.fullmatch(r"(ceiling|held|origin):.+", sv) and sv != "OPEN-AUTHOR":
                rep.fail("C-19", loc(r), f"{cid}: sovereignty {sv!r} is not none, ceiling:T, held:T or origin:T")
            try:
                datetime.date.fromisoformat(r["snapshot_date"])
                if not RE_DATE.match(r["snapshot_date"]):
                    raise ValueError
            except ValueError:
                rep.fail("C-19", loc(r), f"{cid}: snapshot_date {r['snapshot_date']!r} is not YYYY-MM-DD")
            if story_memory is not None:
                lf = r["ledger_file"]
                if lf.strip() == "" or not (story_memory / lf).is_file():
                    rep.fail("C-19", loc(r), f"{cid}: ledger_file {lf!r} does not exist under story-memory/")
    elif not (ct and ct.exists):
        rep.pend("characters.csv not yet generated")

    # ---- C-20 / C-21 kits --------------------------------------------------------------------------------------
    kt = L.tables.get("character-kits.csv")
    if kt and kt.exists and not kt.bad_header:
        seen_k = {}
        for r in kt.rows:
            cid, mid = r["char_id"], r["manual_id"]
            key = (cid, mid)
            if key in seen_k:
                rep.fail("C-20", loc(r), f"duplicate kit row for {cid} and {mid} (first at line {seen_k[key]})")
            seen_k.setdefault(key, r["_line"])
            ch = L.chars.get(cid)
            if ch is None:
                if L.chars or L.file_exists("characters.csv"):
                    rep.fail("C-20", loc(r), f"char_id {cid!r} is not in characters.csv")
                else:
                    rep.pend("kit rows whose characters.csv is not yet generated")
            if cid in ("VRY", "AEG"):
                rep.fail("C-20", loc(r), f"{cid} (Varya, Aegon) must have no kit row (Rule 42.11.7.1)")
            if ch and ch["tier"] in ("C", "D") and r["assign_status"] != "ASKED":
                rep.fail("C-20", loc(r), f"{cid} is Tier {ch['tier']}: a kit row needs assign_status ASKED")
            mi = parse_id(mid)
            if mid not in L.manuals:
                if mi and mi.kind in ("manual", "personal", "found") and not L.file_exists(mi.rel_file):
                    rep.pend("kit rows whose manual file is not yet generated")
                else:
                    rep.fail("C-20", loc(r), f"manual_id {mid!r} does not exist")
            elif mi and mi.kind not in ("manual", "personal", "found"):
                rep.fail("C-20", loc(r), f"manual_id {mid!r} must be a MAN-, PER- or FND- ID")
            kmid = r["kingdom_manual_id"]
            if kmid.strip():
                ki = parse_id(kmid)
                if kmid not in L.kingdom_rows:
                    if ki and ki.kind == "kingdom" and not L.file_exists(ki.rel_file):
                        rep.pend("kit rows whose kingdom file is not yet generated")
                    else:
                        rep.fail("C-20", loc(r), f"kingdom_manual_id {kmid!r} does not exist")
                elif L.kingdom_rows[kmid]["manual_id"] != mid:
                    rep.fail("C-20", loc(r), f"kingdom_manual_id {kmid} points at {L.kingdom_rows[kmid]['manual_id']}, not {mid}")
            if r["learned_via"] not in ("L-1", "L-2"):
                rep.fail("C-20", loc(r), f"learned_via {r['learned_via']!r} is not L-1 or L-2")
            if r["mastery"] not in MASTERY:
                rep.fail("C-20", loc(r), f"mastery {r['mastery']!r} not in {MASTERY}")
            if r["assign_status"] not in ("ASKED", "DERIVED"):
                rep.fail("C-20", loc(r), f"assign_status {r['assign_status']!r} is not ASKED or DERIVED")
            src = r["source"]
            if src.split(":", 1)[0] not in CHANNELS_INST + CHANNELS_FOUND:
                rep.fail("C-20", loc(r), f"source {src!r} does not start with a channel code")
            for tok in split_codes(r["note"]):
                if tok.startswith("COND:") and tok[5:] not in set(COND_CODE.values()):
                    rep.fail("C-20", loc(r), f"note token {tok!r} is not a known condition code")
            # C-21 coherence (INFO)
            man = L.manuals.get(mid)
            if man and ch:
                pw = split_codes(ch["primary_weapons"])
                if pw and man["weapon_id"] not in pw:
                    rep.info("C-21", loc(r), f"{cid} holds {mid} of weapon {man['weapon_id']}, not among primary_weapons {';'.join(pw)}")
    elif not (kt and kt.exists):
        rep.pend("character-kits.csv not yet generated")
    # personal manuals of a Hero/A/B etc. are linked by kits; nothing more to check here
    return rep


def fmt_comp(d):
    return " ".join(f"{TYPE_LETTER[t]}{d[t]}" for t in MOVE_TYPES if t in d)


def cmd_validate(L, C=None, axis="both"):
    rep = Report()
    # self-check: the rounding rule reproduces the fixed table (guards against a damaged copy of the table)
    for (g, n), cell in sorted(COMPOSITION.items()):
        rc = rounded_composition(g, n)
        if rc != cell:
            rep.fail("C-6", "tool", f"internal: Rule 42.2.3.1 gives {rc!r} for {g} N={n}, the table copy says {cell!r}")
    if axis in ("weapon", "both"):
        validate(L, rep)
    if C is not None and axis in ("cultivation", "both"):
        validate_cult(C, L, rep)
    fails = [i for i in rep.items if i[0] == "FAIL"]
    infos = [i for i in rep.items if i[0] == "INFO"]
    for sev, check, where, msg in rep.items:
        print(f"{sev} {check} {where}: {msg}")
    print()
    print("== validate summary ==")
    print(f"root: {L.root}")
    print(f"files read: {len(L.loaded_files)}   weapons: {len(L.weapons)}   generic+personal manuals: {len(L.manuals)}   "
          f"moves: {len(L.moves)}   kingdom rows: {len(L.kingdom_rows)}   characters: {len(L.chars)}   kit rows: {len(L.kits)}")
    by_check = {}
    for sev, check, _, _ in rep.items:
        by_check.setdefault((sev, check), 0)
        by_check[(sev, check)] += 1
    if C is not None and axis in ("cultivation", "both"):
        for line in cult_summary_lines(C):
            print(line)
        if rep.cpend:
            print("not yet generated on the cultivation axis (INFO, not counted as problems):")
            for k, v in sorted(rep.cpend.items()):
                print(f"  {k}: {v}")
    if by_check:
        print("problems by check: " + ", ".join(f"{s} {c} x{n}" for (s, c), n in sorted(by_check.items())))
    if rep.pending or any(L.missing[k] for k in ("manuals", "moves", "kingdoms")):
        print("not yet generated (not counted as problems):")
        nm = len(L.missing["manuals"])
        nv = len(L.missing["moves"])
        if nm or nv:
            print(f"  stock files absent: {nm} manuals files, {nv} moves files "
                  f"(of {len(L.weapon_order) * len(STOCK_GRADES)} each expected)")
        if L.missing["kingdoms"]:
            print(f"  kingdom files absent: {', '.join(L.missing['kingdoms'])}")
        if L.missing["characters"]:
            print("  characters.csv absent")
        if L.missing["character-kits"]:
            print("  character-kits.csv absent")
        for k, v in sorted(rep.pending.items()):
            print(f"  {k}: {v}")
    print("checks not implemented by the tool: C-22 (registered rows) and the C-10 per-grade default comparison")
    if fails:
        counts = {}
        for _, check, _, _ in fails:
            counts[check] = counts.get(check, 0) + 1
        print()
        print("== FAIL count per check ==")
        print("check  count")
        for check in sorted(counts, key=lambda c: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", c)]):
            print(f"{check:<6} {counts[check]}")
        kinds = {}
        for _, check, _, msg in fails:
            m2 = re.sub(r"\b(?:MAN|MV|AZ|GA|PER|FND|CMAN|CMV|CAZ|CGA|PCM)-[A-Z0-9-]+", "ID", msg)
            m2 = re.sub(r"'[^']*'|\"[^\"]*\"", "'..'", m2)
            m2 = re.sub(r"\b(at|in|belongs in) \S+\.csv\S*", r"\1 FILE", m2)
            k = (check, re.sub(r"\d+", "#", m2)[:160])
            kinds[k] = kinds.get(k, 0) + 1
        print()
        print("== 20 most frequent kinds of FAIL (ids, names and numbers masked) ==")
        for (check, shape), n in sorted(kinds.items(), key=lambda kv: (-kv[1], kv[0]))[:20]:
            print(f"{n:>5}  {check}  {shape}")
    print(f"RESULT: {len(fails)} FAIL, {len(infos)} INFO")
    return 1 if fails else 0


# ---------------------------------------------------------------------------------------------------------------
# Cultivation axis (Canon Amendment 2026-10-16): loader, checks C-23 to C-31, affinity command, summary, usable
# ---------------------------------------------------------------------------------------------------------------

def crel(*parts):
    return AXIS_DIR + "/" + "/".join(parts)


class CultLedger:
    """The cultivation axis, read from <root>/cultivation/. Every file may be missing or half written."""

    def __init__(self, root):
        self.root = root
        self.present = (root / AXIS_DIR).is_dir()
        self.tables = {}
        self.loaded_files = []
        self.aff = {}               # affinity_id -> affinities.csv row
        self.codes = list(AFF_CODES)
        self.manuals = {}
        self.moves = {}
        self.moves_by_manual = {}
        self.kingdom_rows = {}
        self.kits = []
        self.chars_ext = {}
        self.absent = {"manuals": 0, "moves": 0}
        self.files_by_aff = {}      # affinity_id -> number of manual/move files present
        if self.present:
            self.load()

    def table(self, rel, canonical):
        t = read_table(self.root, rel, canonical)
        self.tables[rel] = t
        if t.exists:
            self.loaded_files.append(rel)
        return t

    def load(self):
        at = self.table(crel("affinities.csv"), H_CAFF)
        if at.exists and not at.bad_header:
            for r in at.rows:
                if r["affinity_id"] not in self.aff:
                    self.aff[r["affinity_id"]] = r
                    if r["affinity_id"] not in self.codes:
                        self.codes.append(r["affinity_id"])
        for g in GRADE_CODES:
            folder = CODE_TO_FOLDER[g]
            for a in self.codes:
                for kind, hdr in (("manuals", H_CMANUALS), ("moves", H_CMOVES)):
                    t = self.table(crel(kind, folder, f"{a}.csv"), hdr)
                    if t.exists:
                        self.files_by_aff[a] = self.files_by_aff.get(a, 0) + 1
                    else:
                        self.absent[kind] += 1
        for kind, hdr in (("manuals", H_CMANUALS), ("moves", H_CMOVES)):
            for folder in GRADE_FOLDERS:
                d = self.root / AXIS_DIR / kind / folder
                if d.is_dir():
                    for p in sorted(d.glob("*.csv")):
                        rel = crel(kind, folder, p.name)
                        if rel not in self.tables:
                            self.table(rel, hdr)
        for k in ("azorion", "gale"):
            self.table(crel("kingdoms", f"{k}.csv"), H_CKINGDOM)
        pdir = self.root / AXIS_DIR / "personal"
        if pdir.is_dir():
            for p in sorted(pdir.glob("*-manuals.csv")):
                self.table(crel("personal", p.name), H_CPERSONAL)
            for p in sorted(pdir.glob("*-moves.csv")):
                self.table(crel("personal", p.name), H_CMOVES)
        kt = self.table(crel("kits.csv"), H_CKITS)
        ct = self.table(crel("characters-ext.csv"), H_CCHARS)
        for rel, t in self.tables.items():
            if t.bad_header or not t.exists:
                continue
            if "/manuals/" in rel or rel.endswith("-manuals.csv"):
                for r in t.rows:
                    self.manuals.setdefault(r["manual_id"], r)
            elif "/moves/" in rel or rel.endswith("-moves.csv"):
                for r in t.rows:
                    self.moves.setdefault(r["move_id"], r)
                    self.moves_by_manual.setdefault(r["manual_id"], []).append(r)
            elif "/kingdoms/" in rel:
                for r in t.rows:
                    self.kingdom_rows.setdefault(r["kingdom_id"], r)
        if kt.exists and not kt.bad_header:
            self.kits = kt.rows
        if ct.exists and not ct.bad_header:
            for r in ct.rows:
                self.chars_ext.setdefault(r["char_id"], r)

    def file_exists(self, rel):
        t = self.tables.get(rel)
        return bool(t and t.exists)

    def counts(self, a):
        """(nine class counts, source label) for a discipline: affinities.csv row first, else the design class table."""
        r = self.aff.get(a)
        keys = ("basic_n", "inter_n", "adv_common_n", "adv_kingdom_n", "elite_n", "sig_n", "fus_n", "cat_n", "myt_n")
        if r:
            try:
                return tuple(int(r[k]) for k in keys), "affinities.csv"
            except ValueError:
                return None, "affinities.csv (non-integer count)"
        cls = AFF_CLASS.get(a)
        if cls:
            return CLASS_COUNTS[cls], "design table (affinities.csv not yet present)"
        return None, "unknown discipline"

    def req_kind(self, a):
        r = self.aff.get(a)
        return (r["req_kind"] if r and r.get("req_kind") else AFF_KIND.get(a))


def cult_grade_rows(c, g):
    """Rows expected in the manuals file of one grade for counts tuple c."""
    return {"BAS": c[0], "INT": c[1], "ADV": c[2] + 2 * c[3], "ELI": 2 * c[4], "SIG": 2 * c[5],
            "FUS": c[6], "CAT": c[7], "MYT": c[8]}[g]


def cult_expected_origin(g, n, c):
    if g == "ADV":
        return "Common" if n <= c[2] else ("Azorion" if n <= c[2] + c[3] else "Gale")
    if g == "ELI":
        return "Azorion" if n <= c[4] else "Gale"
    if g == "SIG":
        return "Azorion" if n <= c[5] else "Gale"
    return "Common"


def cult_file_complete(C, g, a):
    """True when the manuals file, its moves file and every manual's moves are all fully present."""
    folder = CODE_TO_FOLDER[g]
    mt = C.tables.get(crel("manuals", folder, f"{a}.csv"))
    vt = C.tables.get(crel("moves", folder, f"{a}.csv"))
    if not (mt and mt.exists and vt and vt.exists) or mt.bad_header or vt.bad_header or not mt.rows:
        return False
    c, _ = C.counts(a)
    if c is not None and len(mt.rows) != cult_grade_rows(c, g):
        return False
    for r in mt.rows:
        if not r["move_count"].isdigit() or len(C.moves_by_manual.get(r["manual_id"], [])) != int(r["move_count"]):
            return False
    return True


def validate_cult(C, W, rep):
    """Checks C-23 to C-31. Missing or partial files are counted in rep.cpending, never failed."""
    if not C.present:
        return
    story_memory = C.root.parent if C.root.parent.name == "story-memory" else None
    cp = rep.cpend

    # ---- C-23 headers, format, plain text, affinities.csv, kits, characters-ext -------------------------------
    for rel, t in C.tables.items():
        if not t.exists:
            continue
        if t.bad_header and t.header:
            rep.fail("C-23", f"{rel}:1", "header line differs from the canonical header; file skipped by later checks")
        for line, msg in t.format_problems:
            rep.fail("C-23", f"{rel}:{line}", msg)
        if t.bad_header:
            continue
        for r in t.rows:
            for k in t.header:
                v = r.get(k, "")
                bad = []
                if "*" in v:
                    bad.append("asterisk")
                if "`" in v:
                    bad.append("backtick")
                if "\t" in v:
                    bad.append("tab")
                if RE_UNDERSCORE_MARK.search(v):
                    bad.append("underscore mark-up")
                if EM_DASH in v and k != "first_area":
                    bad.append("em dash")
                if bad:
                    rep.fail("C-23", loc(r), f"column {k} holds {', '.join(bad)}: {v[:50]!r}")
    at = C.tables.get(crel("affinities.csv"))
    if at and at.exists and not at.bad_header:
        seen = {}
        for r in at.rows:
            a = r["affinity_id"]
            if a in seen:
                rep.fail("C-23", loc(r), f"duplicate affinity_id {a} (first at line {seen[a]})")
            seen.setdefault(a, r["_line"])
            if a not in AFF_CLASS:
                rep.fail("C-23", loc(r), f"affinity_id {a!r} is not one of the 65 disciplines of the design")
                continue
            for k in ("basic_n", "inter_n", "adv_n", "adv_common_n", "adv_kingdom_n", "elite_n", "sig_n", "fus_n", "cat_n", "myt_n"):
                if not r[k].isdigit():
                    rep.fail("C-23", loc(r), f"{a}: {k} is not an integer: {r[k]!r}")
            if r["req_kind"] != AFF_KIND[a]:
                rep.fail("C-23", loc(r), f"{a}: req_kind {r['req_kind']!r} differs from the design's {AFF_KIND[a]}")
            if r["prominence"] != AFF_CLASS[a]:
                rep.info("C-23", loc(r), f"{a}: prominence {r['prominence']!r} differs from the design's {AFF_CLASS[a]}")
            if r["support_role"] not in ("Primary", "Secondary", "Minor"):
                rep.fail("C-23", loc(r), f"{a}: support_role {r['support_role']!r} not Primary, Secondary or Minor")
        if len(at.rows) < len(AFF_CODES):
            cp["disciplines missing from affinities.csv"] = len(AFF_CODES) - len(at.rows)
    else:
        cp["affinities.csv absent (design class counts are used)"] = 1
    kt = C.tables.get(crel("kits.csv"))
    if kt and kt.exists and not kt.bad_header:
        seen_k = {}
        for r in kt.rows:
            cid, mid = r["char_id"], r["manual_id"]
            if (cid, mid) in seen_k:
                rep.fail("C-23", loc(r), f"duplicate kit row for {cid} and {mid} (first at line {seen_k[(cid, mid)]})")
            seen_k.setdefault((cid, mid), r["_line"])
            if W.chars and cid not in W.chars:
                rep.fail("C-23", loc(r), f"char_id {cid!r} is not in characters.csv")
            mi = parse_id(mid)
            if not (mi and mi.axis == "cultivation" and mi.kind in ("manual", "personal")):
                rep.fail("C-23", loc(r), f"manual_id {mid!r} must be a CMAN- or PCM- ID")
            elif mid not in C.manuals:
                if C.file_exists(mi.rel_file):
                    rep.fail("C-23", loc(r), f"manual_id {mid!r} does not exist")
                else:
                    cp["kit rows whose manual file is not yet generated"] = cp.get("kit rows whose manual file is not yet generated", 0) + 1
            if r["learned_via"] not in ("L-1", "L-2"):
                rep.fail("C-23", loc(r), f"learned_via {r['learned_via']!r} is not L-1 or L-2")
            if r["mastery"] not in MASTERY:
                rep.fail("C-23", loc(r), f"mastery {r['mastery']!r} not in {MASTERY}")
            if r["assign_status"] not in ("ASKED", "DERIVED"):
                rep.fail("C-23", loc(r), f"assign_status {r['assign_status']!r} is not ASKED or DERIVED")
    ce = C.tables.get(crel("characters-ext.csv"))
    if ce and ce.exists and not ce.bad_header and W.chars:
        for r in ce.rows:
            if r["char_id"] not in W.chars:
                rep.fail("C-23", loc(r), f"char_id {r['char_id']!r} is not in characters.csv")

    # ---- manuals: C-24, C-25, C-26, C-27 ------------------------------------------------------------------------
    seen_ids = {}

    def dup(idv, r):
        if idv in seen_ids:
            rep.fail("C-24", loc(r), f"duplicate ID {idv} (first at {seen_ids[idv]})")
        else:
            seen_ids[idv] = loc(r)

    mtabs = [(rel, t) for rel, t in C.tables.items() if t.exists and not t.bad_header and (
        "/manuals/" in rel or rel.endswith("-manuals.csv"))]
    vtabs = [(rel, t) for rel, t in C.tables.items() if t.exists and not t.bad_header and (
        "/moves/" in rel or rel.endswith("-moves.csv"))]
    early = {}
    for rel, t in mtabs:
        generic = "/manuals/" in rel
        parts = rel.split("/")
        pchar = None if generic else parts[2].split("-")[0].upper()
        prev = 0
        for r in t.rows:
            mid = r["manual_id"]
            dup(mid, r)
            info = parse_id(mid)
            a = r["affinity_id"]
            grade = r["grade"]
            counts = None
            if generic:
                if not info or info.kind != "manual" or info.axis != "cultivation":
                    rep.fail("C-24", loc(r), f"manual_id {mid!r} is not a CMAN-GRD-AFF-NNN ID")
                else:
                    if info.rel_file != rel:
                        rep.fail("C-24", loc(r), f"{mid} belongs in {info.rel_file}")
                    if grade != info.grade:
                        rep.fail("C-24", loc(r), f"{mid}: grade cell {grade!r} differs from ID grade {info.grade}")
                    if a != info.wpn:
                        rep.fail("C-24", loc(r), f"{mid}: affinity_id {a!r} differs from ID discipline {info.wpn}")
                    n = int(info.nnn)
                    if n != prev + 1:
                        rep.fail("C-24", loc(r), f"{mid}: number {info.nnn} is not contiguous (expected {prev + 1:03d})")
                    prev = n
                    counts, _ = C.counts(info.wpn)
                    if info.wpn not in C.codes:
                        rep.fail("C-24", loc(r), f"{mid}: discipline {info.wpn} is not one of the 65")
                    elif counts is not None:
                        eo = cult_expected_origin(info.grade, n, counts)
                        if r["origin"] != eo:
                            rep.fail("C-24", loc(r), f"{mid}: origin {r['origin']!r}, number order expects {eo}")
                        if n > cult_grade_rows(counts, info.grade):
                            rep.fail("C-24", loc(r), f"{mid}: number {n} is beyond the {cult_grade_rows(counts, info.grade)} rows the counts give {info.wpn} {info.grade}")
                    if r["origin"] not in ("Common", "Azorion", "Gale"):
                        rep.fail("C-24", loc(r), f"{mid}: cultivation origin {r['origin']!r} must be Common, Azorion or Gale")
            else:
                if not info or info.kind != "personal" or info.axis != "cultivation":
                    rep.fail("C-24", loc(r), f"manual_id {mid!r} is not a PCM-CHR-NN ID")
                else:
                    if info.chr != pchar:
                        rep.fail("C-24", loc(r), f"{mid}: character code {info.chr} differs from the file's {pchar}")
                    if r["owner"] != info.chr:
                        rep.fail("C-24", loc(r), f"{mid}: owner {r['owner']!r} differs from ID character {info.chr}")
                    n = int(info.nn)
                    if n != prev + 1:
                        rep.fail("C-24", loc(r), f"{mid}: number {info.nn} is not contiguous (expected {prev + 1:02d})")
                    prev = n
                    if W.chars and r["owner"] not in W.chars:
                        rep.fail("C-24", loc(r), f"{mid}: owner {r['owner']!r} is not in characters.csv")
                    if r["origin"] not in ("Personal", "Olympus"):
                        rep.fail("C-24", loc(r), f"{mid}: personal origin {r['origin']!r} must be Personal or Olympus")
                    if r.get("source", "").split(":", 1)[0] not in CHANNELS_INST + CHANNELS_FOUND:
                        rep.fail("C-24", loc(r), f"{mid}: source {r.get('source')!r} does not start with a channel code")
                if grade not in GRADE_CODES:
                    rep.fail("C-24", loc(r), f"{mid}: grade {grade!r} is not one of {' '.join(GRADE_CODES)}")
                if a not in C.codes:
                    rep.fail("C-24", loc(r), f"{mid}: affinity_id {a!r} is not one of the 65")
            if r["status"] not in STATUSES:
                rep.fail("C-16", loc(r), f"{mid}: status {r['status']!r} not in {STATUSES}")
            fa = r["first_area"]
            if fa != DEFAULT_FIRST_AREA and not RE_FIRST_AREA.match(fa):
                rep.fail("C-16", loc(r), f"{mid}: first_area {fa!r} is neither 'Not yet established' nor the Area form")
            if r["origin"] not in ORIGINS:
                rep.fail("C-24", loc(r), f"{mid}: origin {r['origin']!r} not in {ORIGINS}")
            # C-25 realm floor, band, window
            band = r["realm_band"]
            mp = realm_pos(r["min_realm"])
            if band not in BANDS:
                rep.fail("C-25", loc(r), f"{mid}: realm_band {band!r} not in {BANDS}")
            if mp is None:
                rep.fail("C-25", loc(r), f"{mid}: min_realm {r['min_realm']!r} is not '<Realm> L<n> <Low|Mid|High|Peak>'")
            else:
                if mp < realm_pos(CFLOOR):
                    rep.fail("C-25", loc(r), f"{mid}: min_realm {r['min_realm']} is below the cultivation floor {CFLOOR}")
                rb = realm_band(r["min_realm"])
                if band in BANDS and rb != band:
                    rep.fail("C-25", loc(r), f"{mid}: min_realm {r['min_realm']} is in band {rb}, realm_band says {band}")
                windows = CWINDOWS_SR if AFF_KIND.get(a) == "SR" else CWINDOWS
                win = windows.get((grade, band)) if grade in GRADE_CODES else None
                if AFF_KIND.get(a) == "SR" and grade == "BAS" and band == "M2":
                    win = [EARLY_AWAKENING]          # the Early Awakening exception (Part 4 Area 2.4)
                    early[a] = early.get(a, 0) + 1
                if win:
                    if not any(realm_pos(lo) <= mp <= realm_pos(hi) for lo, hi in win):
                        rep.fail("C-25", loc(r), f"{mid}: min_realm {r['min_realm']} is outside the window {win[0][0]} to {win[0][1]} for {grade} {band}")
                elif band in BANDS and grade in GRADE_CODES:
                    rep.fail("C-25", loc(r), f"{mid}: no cultivation window exists for grade {grade} in band {band}")
                low_err = check_unlock_floor(mp, C.moves_by_manual.get(mid, []))
                if low_err:
                    rep.fail("C-25", loc(r), f"{mid}: {low_err}")
            # C-26 requirement cells
            e, cs, ar, sv = r["energy_req"], r["cultivation_req"], r["affinity_req"], r["sovereignty_req"]
            kind = C.req_kind(a)
            fus_law = FUSION_REQ.get(band) if grade == "FUS" else None   # Part 42 Area 6 Fusion rows
            if fus_law:
                if cs != fus_law[0]:
                    rep.fail("C-26", loc(r), f"{mid}: cultivation_req {cs!r} must be {fus_law[0]} for FUS in band {band}")
                if kind == "A" and ar != "A4+A4":
                    rep.fail("C-26", loc(r), f"{mid}: affinity_req {ar!r} must be A4+A4 for a Fusion manual")
                if kind != "A" and ar not in ("A4+A4", "NONE") and (kind == "SR" and ar not in SR_CODES or kind == "HL" and ar not in HL_CODES):
                    rep.fail("C-26", loc(r), f"{mid}: affinity_req {ar!r} is not lawful for a Fusion manual")
                if e != "QI-VHI":
                    rep.fail("C-26", loc(r), f"{mid}: energy_req {e!r} must be QI-VHI for FUS")
                if sv != fus_law[1]:
                    rep.fail("C-26", loc(r), f"{mid}: sovereignty_req {sv!r} must be {fus_law[1]} for FUS in band {band}")
            elif kind == "A":
                m = re.fullmatch(r"A([2-7])", ar)
                if not m:
                    rep.fail("C-26", loc(r), f"{mid}: affinity_req {ar!r} must be A2 to A7 (never NONE, no W suffix) for an affinity discipline")
                elif band in A_BAND_CAP:
                    cap = A_BAND_CAP[band]
                    if int(m.group(1)) > cap and not (band == "CF" and m.group(1) == "7" and realm_name(r["min_realm"]) == "Core Solidification"):
                        rep.fail("C-26", loc(r), f"{mid}: affinity_req {ar} is above the band {band} cap A{cap}")
            elif kind == "SR":
                if ar not in SR_CODES:
                    rep.fail("C-26", loc(r), f"{mid}: affinity_req {ar!r} must be SR1 to SR12 for a soul-type discipline")
            elif kind == "HL":
                if ar not in HL_CODES:
                    rep.fail("C-26", loc(r), f"{mid}: affinity_req {ar!r} must be HL1 to HL5 for the Heart discipline")
            elif kind == "NONE":
                if ar != "NONE":
                    rep.fail("C-26", loc(r), f"{mid}: affinity_req {ar!r} must be NONE for {a}")
            if e not in ENERGY_LADDER:
                rep.fail("C-26", loc(r), f"{mid}: energy_req {e!r} not in the ladder")
            cparts = cs.split("+")
            if fus_law:
                pass                      # Fusion cultivation_req already checked against its law row above
            elif cparts[0] not in CULT_STATES or cparts[0] == "NONE" or cparts[0].startswith("T1-"):
                rep.fail("C-26", loc(r), f"{mid}: cultivation_req state {cparts[0]!r} must be CIRC or higher on this axis")
            for lk in ([] if fus_law else cparts[1:]):
                if lk not in CULT_LINKS:
                    rep.fail("C-26", loc(r), f"{mid}: cultivation_req link {lk!r} not in the link codes")
            if sv not in SOV_CODES:
                rep.fail("C-26", loc(r), f"{mid}: sovereignty_req {sv!r} not in the ladder")
            if r["tradition"].strip() == "":
                rep.fail("C-27", loc(r), f"{mid}: tradition is empty")
            if r["title"].strip() == "":
                rep.fail("C-27", loc(r), f"{mid}: title is empty")
            # C-27 count and composition
            mc = r["move_count"]
            if not mc.isdigit():
                rep.fail("C-27", loc(r), f"{mid}: move_count {mc!r} is not an integer")
                continue
            mcn = int(mc)
            if not 5 <= mcn <= 15:
                rep.fail("C-27", loc(r), f"{mid}: move_count {mcn} is outside 5 to 15")
            if grade in COUNT_RANGE and 5 <= mcn <= 15:
                lo, hi = COUNT_RANGE[grade]
                if not lo <= mcn <= hi:
                    rep.fail("C-27", loc(r), f"{mid}: move_count {mcn} is outside the {grade} range {lo} to {hi}")
                tbl = COMPOSITION.get((grade, mcn))
                if r["composition"] != tbl:
                    rep.fail("C-27", loc(r), f"{mid}: composition {r['composition']!r} differs from the Part 42 table cell {tbl!r} for {grade} N={mcn}")
                pc = parse_comp(r["composition"])
                moves = C.moves_by_manual.get(mid)
                mrel = manual_moves_file(info) if info else None
                if moves is None:
                    if mrel and C.file_exists(mrel):
                        cp["manuals with no move rows yet (moves file still being written)"] = cp.get("manuals with no move rows yet (moves file still being written)", 0) + 1
                    else:
                        cp["manuals whose moves file is not yet generated"] = cp.get("manuals whose moves file is not yet generated", 0) + 1
                else:
                    if len(moves) > mcn:
                        rep.fail("C-27", loc(r), f"{mid}: move_count {mcn} but {len(moves)} move rows exist")
                    elif len(moves) < mcn:
                        cp["manuals with fewer move rows than move_count (still being written?)"] = cp.get("manuals with fewer move rows than move_count (still being written?)", 0) + 1
                    actual = {}
                    for mv in moves:
                        actual[mv["move_type"]] = actual.get(mv["move_type"], 0) + 1
                    if len(moves) == mcn and pc is not None and actual != pc:
                        rep.fail("C-27", loc(r), f"{mid}: move_type counts {fmt_comp(actual)} differ from composition {r['composition']!r}")
    for a, n in sorted(early.items()):
        if n > 1:
            rep.info("C-25", crel("manuals", "basic", f"{a}.csv"), f"{a}: {n} Early Awakening Basic manuals at Monarch (design allows one per soul type)")
    # C-24 row counts per discipline and grade
    for g in GRADE_CODES:
        folder = CODE_TO_FOLDER[g]
        for a in C.codes:
            rel = crel("manuals", folder, f"{a}.csv")
            t = C.tables.get(rel)
            counts, _src = C.counts(a)
            if counts is None:
                if a in C.aff:
                    rep.fail("C-24", crel("affinities.csv"), f"{a}: count columns are not integers")
                continue
            exp = cult_grade_rows(counts, g)
            if not t or not t.exists:
                cp[f"manual files ({g}) not yet generated"] = cp.get(f"manual files ({g}) not yet generated", 0) + 1
                continue
            if t.bad_header:
                continue
            got = len(t.rows)
            if got == exp:
                continue
            if got < exp:
                cp[f"manual files ({g}) with fewer rows than expected (still being written?)"] = cp.get(f"manual files ({g}) with fewer rows than expected (still being written?)", 0) + 1
            else:
                rep.fail("C-24", rel, f"{a} {g}: {got} manual rows, the counts give {exp}")

    # ---- moves: C-27 (ids, seq, order), C-28 (fields) -----------------------------------------------------------
    for rel, t in vtabs:
        generic = "/moves/" in rel
        parts = rel.split("/")
        for r in t.rows:
            mvid = r["move_id"]
            dup(mvid, r)
            info = parse_id(mvid)
            mid = r["manual_id"]
            minfo = parse_id(mid)
            if generic:
                if not info or info.kind != "move" or info.axis != "cultivation":
                    rep.fail("C-27", loc(r), f"move_id {mvid!r} is not a CMV-GRD-AFF-NNN-SS ID")
                elif info.rel_file != rel:
                    rep.fail("C-27", loc(r), f"{mvid} belongs in {info.rel_file}")
                elif r["affinity_id"] != info.wpn:
                    rep.fail("C-27", loc(r), f"{mvid}: affinity_id {r['affinity_id']!r} differs from ID discipline {info.wpn}")
            else:
                if not info or info.kind != "personal_move" or info.axis != "cultivation":
                    rep.fail("C-27", loc(r), f"move_id {mvid!r} is not a PCM-CHR-NN-SS ID")
                elif info.chr != parts[2].split("-")[0].upper():
                    rep.fail("C-27", loc(r), f"{mvid} belongs in cultivation/personal/{info.chr.lower()}-moves.csv")
            if info and info.manual_id != mid:
                rep.fail("C-27", loc(r), f"{mvid}: manual_id {mid!r} differs from the ID prefix {info.manual_id}")
            if info and r["seq"] != info.seq:
                rep.fail("C-27", loc(r), f"{mvid}: seq {r['seq']!r} differs from the ID suffix {info.seq}")
            if not re.fullmatch(r"\d{2}", r["seq"]):
                rep.fail("C-27", loc(r), f"{mvid}: seq {r['seq']!r} is not two digits")
            man = C.manuals.get(mid)
            if man is None:
                if minfo and not C.file_exists(minfo.rel_file):
                    cp["move rows whose manuals file is not yet generated"] = cp.get("move rows whose manuals file is not yet generated", 0) + 1
                elif minfo and minfo.kind == "manual":
                    cp["move rows whose manual row is not yet written"] = cp.get("move rows whose manual row is not yet written", 0) + 1
                else:
                    rep.fail("C-27", loc(r), f"{mvid}: manual_id {mid} has no manual row")
            mt = r["move_type"]
            if mt not in MOVE_TYPES:
                rep.fail("C-28", loc(r), f"{mvid}: move_type {mt!r} not in {MOVE_TYPES}")
                continue
            if man:
                comp = parse_comp(man["composition"])
                if comp is not None and mt not in comp:
                    rep.fail("C-27", loc(r), f"{mvid}: move_type {mt} is not in the manual's composition {man['composition']!r}")
                if man["grade"] in GRADE_PERCENTS and mt not in GRADE_PERCENTS[man["grade"]]:
                    rep.fail("C-27", loc(r), f"{mvid}: move_type {mt} is not a type of grade {man['grade']}")
            if r["name"].strip() == "":
                rep.fail("C-28", loc(r), f"{mvid}: name is empty")
            if r["status"] not in STATUSES:
                rep.fail("C-16", loc(r), f"{mvid}: status {r['status']!r} not in {STATUSES}")
            fa = r["first_area"]
            if fa != DEFAULT_FIRST_AREA and not RE_FIRST_AREA.match(fa):
                rep.fail("C-16", loc(r), f"{mvid}: first_area {fa!r} is neither 'Not yet established' nor the Area form")
            fn = r["function"]
            prim, _, sec = fn.partition("|")
            for part, label in ((prim, "primary"), (sec, "secondary")):
                if part == "" and label == "secondary" and "|" not in fn:
                    continue
                m = RE_FUNCTION.match(part)
                if not m or m.group("c") not in FUNCTIONS_C or m.group("s") not in FUNCTIONS_C[m.group("c")]:
                    rep.fail("C-28", loc(r), f"{mvid}: {label} function {part!r} is not a Part 6 Category:Sub (Support also has Revive, Cleanse)")
                    continue
                sub = m.group("s")
                rank = TYPE_RANK[mt]
                if sub in ("Absorb", "Flash", "Phase", "TrueDamage") and rank < TYPE_RANK["Elite"]:
                    rep.fail("C-28", loc(r), f"{mvid}: function {part} appears only in Elite or above (move is {mt})")
                if sub == "Revive" and rank < TYPE_RANK["Advanced"]:
                    rep.fail("C-28", loc(r), f"{mvid}: Revive appears only in Advanced or above (move is {mt})")
                if sub == "Cleanse" and rank < TYPE_RANK["Intermediate"]:
                    rep.fail("C-28", loc(r), f"{mvid}: Cleanse appears only in Intermediate or above (move is {mt})")
                if sub == "Convergence" and mt != "Fusion":
                    rep.fail("C-28", loc(r), f"{mvid}: Convergence appears only in a Fusion-type move")
                if sub in ("Formation", "Trap") and rank < TYPE_RANK["Advanced"]:
                    rep.fail("C-28", loc(r), f"{mvid}: {sub} appears only in Advanced or above (move is {mt})")
            if r["form"] not in FORMS:
                rep.fail("C-28", loc(r), f"{mvid}: form {r['form']!r} not in {FORMS}")
            elif r["form"] not in FORM_ALLOWED[mt]:
                rep.fail("C-28", loc(r), f"{mvid}: a {mt} move may not take form {r['form']}")
            if r["cost_class"] not in COST_CLASSES:
                rep.fail("C-28", loc(r), f"{mvid}: cost_class {r['cost_class']!r} not in {COST_CLASSES}")
            elif r["cost_class"] not in COST_RANGE[mt]:
                rep.fail("C-28", loc(r), f"{mvid}: cost_class {r['cost_class']} is outside {COST_RANGE[mt]} for {mt}")
            ok_unlock = {UNLOCK_REALM[mt], max(UNLOCK_REALM[mt], CFLOOR, key=realm_pos)}  # table value, or lifted to the Warrior floor
            if r["unlock_realm"] not in ok_unlock:
                rep.fail("C-28", loc(r), f"{mvid}: unlock_realm {r['unlock_realm']!r} must be one of {sorted(ok_unlock)} for {mt}")
            if mt == "Fusion" and not r["description"].startswith("streams:"):
                rep.fail("C-28", loc(r), f"{mvid}: a Fusion move's description must begin 'streams:'")
    for mid, rows in C.moves_by_manual.items():
        rs = sorted(rows, key=lambda r: (r["seq"], r["_line"]))
        seqs = [r["seq"] for r in rs]
        want = [f"{i:02d}" for i in range(1, len(rows) + 1)]
        if seqs != want:
            rep.fail("C-27", f"{rows[0]['_file']}:{rows[0]['_line']}", f"{mid}: seq values {','.join(seqs)} are not contiguous 01..{len(rows):02d}")
        if [r["seq"] for r in rows] != sorted(r["seq"] for r in rows):
            rep.fail("C-27", f"{rows[0]['_file']}:{rows[0]['_line']}", f"{mid}: move rows are not in seq order inside the file")
        ranks = [TYPE_RANK.get(r["move_type"], 0) for r in rs]
        if ranks != sorted(ranks):
            rep.fail("C-27", f"{rows[0]['_file']}:{rows[0]['_line']}", f"{mid}: moves do not run lowest type first")

    # ---- kingdom rows (numbered C-24 with the counts) -----------------------------------------------------------
    inst_forms = [(compare_form(i)[4:] if compare_form(i).startswith("the ") else compare_form(i)) for i in INSTITUTIONS]
    by_kingdom = {"azorion": {}, "gale": {}}
    for kf, kname, pref in (("azorion", "Azure Sky", "CAZ"), ("gale", "Gale", "CGA")):
        t = C.tables.get(crel("kingdoms", f"{kf}.csv"))
        if not t or not t.exists or t.bad_header:
            continue
        for r in t.rows:
            kid = r["kingdom_id"]
            dup(kid, r)
            info = parse_id(kid)
            if not info or info.kind != "kingdom" or info.axis != "cultivation":
                rep.fail("C-24", loc(r), f"kingdom_id {kid!r} is not a CAZ-/CGA- ID")
            else:
                if info.king != pref:
                    rep.fail("C-24", loc(r), f"{kid} belongs in the other kingdom file")
                if info.manual_id != r["manual_id"]:
                    rep.fail("C-24", loc(r), f"{kid}: manual_id {r['manual_id']} differs from the ID's {info.manual_id}")
            if r["kingdom"] != kname:
                rep.fail("C-24", loc(r), f"{kid}: kingdom {r['kingdom']!r} must be {kname!r} in this file")
            if r["channel"] not in CHANNELS_INST:
                rep.fail("C-24", loc(r), f"{kid}: channel {r['channel']!r} not in {CHANNELS_INST}")
            if r["access"] not in ACCESS_CODES:
                rep.fail("C-24", loc(r), f"{kid}: access {r['access']!r} not in {ACCESS_CODES}")
            if r["copy_control"] not in COPY_CODES:
                rep.fail("C-24", loc(r), f"{kid}: copy_control {r['copy_control']!r} not in {COPY_CODES}")
            if r["status"] not in STATUSES:
                rep.fail("C-16", loc(r), f"{kid}: status {r['status']!r} not in {STATUSES}")
            inst = r["institution"]
            if not inst.startswith("OPEN-AUTHOR"):
                f2 = compare_form(inst)
                f2 = f2[4:] if f2.startswith("the ") else f2
                if not any(f2 == i or i in f2 or f2 in i for i in inst_forms if f2):
                    rep.fail("C-17", loc(r), f"{kid}: institution {inst!r} is not in the Rule 42.7.2.2 list and does not begin OPEN-AUTHOR")
            man = C.manuals.get(r["manual_id"])
            if man is None:
                mi = parse_id(r["manual_id"])
                if mi and not C.file_exists(mi.rel_file):
                    cp["kingdom rows whose manuals file is not yet generated"] = cp.get("kingdom rows whose manuals file is not yet generated", 0) + 1
                else:
                    rep.fail("C-24", loc(r), f"{kid}: manual_id {r['manual_id']} has no manual row")
            else:
                o = man["origin"]
                if not (o == "Common" or (o == "Azorion" and kf == "azorion") or (o == "Gale" and kf == "gale")):
                    rep.fail("C-24", loc(r), f"{kid}: a kingdom row never points at a manual of origin {o} ({r['manual_id']})")
            if r["manual_id"] in by_kingdom[kf]:
                rep.fail("C-24", loc(r), f"{kid}: manual {r['manual_id']} already has a row in this kingdom file")
            by_kingdom[kf][r["manual_id"]] = r
    for mid, man in C.manuals.items():
        if not mid.startswith("CMAN-") or man["grade"] in HEADER_ONLY_GRADES:
            continue  # Fusion, Catastrophic, Mythic are Common-origin with no kingdom rows (OPEN-3)
        o = man["origin"]
        need = ["azorion"] if o == "Azorion" else ["gale"] if o == "Gale" else ["azorion", "gale"] if o == "Common" else []
        for kf in need:
            if not C.file_exists(crel("kingdoms", f"{kf}.csv")):
                cp[f"manuals awaiting a {kf} kingdom row (file not yet generated)"] = cp.get(f"manuals awaiting a {kf} kingdom row (file not yet generated)", 0) + 1
            elif mid not in by_kingdom[kf]:
                rep.fail("C-24", f"{man['_file']}:{man['_line']}", f"{mid} ({o}) has no row in cultivation/kingdoms/{kf}.csv")

    # ---- C-29 Support quota (only for a discipline whose eight grades are complete) --------------------------------
    for a in C.codes:
        if not all(cult_file_complete(C, g, a) for g in GRADE_CODES):
            if C.files_by_aff.get(a):
                cp["disciplines not yet complete (Support quota and three-word share waiting)"] = cp.get("disciplines not yet complete (Support quota and three-word share waiting)", 0) + 1
            continue
        moves = [mv for mid, mvs in C.moves_by_manual.items() for mv in mvs if mv.get("affinity_id") == a]
        if not moves:
            continue
        role_cell = C.aff[a]["support_role"] if a in C.aff else ("Primary" if a in SUPPORT_PRIMARY else "Secondary" if a in SUPPORT_SECONDARY else "Minor")
        if role_cell == "Minor":
            continue
        only = SECONDARY_ONLY.get(a)
        sup = heal = 0
        for mv in moves:
            pm = RE_FUNCTION.match(mv["function"].partition("|")[0])
            if pm and pm.group("c") == "Support":
                if only is None or pm.group("s") in only:
                    sup += 1
                if pm.group("s") in HEALING_FUNCS:
                    heal += 1
        share = sup / len(moves)
        target = 0.5 if role_cell == "Primary" else 0.15
        where = crel("moves", "*", f"{a}.csv")
        if share < target / 2:
            rep.fail("C-29", where, f"{a}: Support share {share:.0%} is below half of the {role_cell} target {target:.0%}")
        elif share < target:
            rep.info("C-29", where, f"{a}: Support share {share:.0%} is below the {role_cell} target {target:.0%}")
        if SUPPORT_PRIMARY.get(a) == "heal" and role_cell == "Primary":
            hs = heal / len(moves)
            if hs < 0.15:
                rep.fail("C-29", where, f"{a}: Heal, Revive and Cleanse share {hs:.0%} is below half of the 30% healing target")
            elif hs < 0.30:
                rep.info("C-29", where, f"{a}: Heal, Revive and Cleanse share {hs:.0%} is below the 30% healing target")

    # ---- C-30 Move-Naming Law ---------------------------------------------------------------------------------------
    for rel, t in vtabs:
        if not t.rows:
            continue
        three = 0
        for r in t.rows:
            w = len(r["name"].split())
            if w >= 4:
                rep.fail("C-30", loc(r), f"{r['move_id']}: name {r['name']!r} has {w} words (one to three allowed)")
            elif w == 3:
                three += 1
        pm = re.match(rf"{AXIS_DIR}/moves/(\w+)/(\w{{3}})\.csv$", rel)
        if not pm:
            continue
        g, a = FOLDER_TO_CODE.get(pm.group(1)), pm.group(2)
        if g is None or not cult_file_complete(C, g, a):
            continue
        n = len(t.rows)
        if g in HEADER_ONLY_GRADES:
            if three * 2 > n:
                rep.fail("C-30", rel, f"{a} {g}: {three} of {n} names have three words, more than half")
        elif three > (n * 5) // 100:
            rep.fail("C-30", rel, f"{a} {g}: {three} of {n} names have three words, the limit is {(n * 5) // 100} (5 percent rounded down)")

    # ---- C-31 uniqueness across both axes ---------------------------------------------------------------------------
    names, titles = {}, {}
    for r in W.manuals.values():
        titles.setdefault(compare_form(r["title"]), []).append(r)
    for r in W.moves.values():
        names.setdefault(compare_form(r["name"]), []).append(r)
    for r in C.manuals.values():
        titles.setdefault(compare_form(r["title"]), []).append(r)
    for r in C.moves.values():
        names.setdefault(compare_form(r["name"]), []).append(r)

    def is_c(r):
        return r["_file"].startswith(AXIS_DIR + "/")
    for form, rows in names.items():
        if form and len(rows) > 1:
            for r in rows[1:]:
                if is_c(r) or is_c(rows[0]):
                    rep.fail("C-31", loc(r), f"move name {r['name']!r} duplicates {rows[0]['move_id']} at {loc(rows[0])}")
        if form in titles and any(is_c(r) for r in rows + titles[form]):
            for r in rows:
                rep.fail("C-31", loc(r), f"move name {r['name']!r} equals manual title of {titles[form][0]['manual_id']}")
        if form and (form[4:] if form.startswith("the ") else form) in inst_forms:
            for r in rows:
                if is_c(r):
                    rep.fail("C-31", loc(r), f"move name {r['name']!r} equals an institution name")
    for form, rows in titles.items():
        if form and len(rows) > 1:
            for r in rows[1:]:
                if is_c(r) or is_c(rows[0]):
                    rep.fail("C-31", loc(r), f"manual title {r['title']!r} duplicates {rows[0]['manual_id']} at {loc(rows[0])}")
        if form and (form[4:] if form.startswith("the ") else form) in inst_forms:
            for r in rows:
                if is_c(r):
                    rep.fail("C-31", loc(r), f"manual title {r['title']!r} equals an institution name")


def cult_summary_lines(C):
    """INFO lines for the validate summary: counts only, never problems."""
    if not C.present:
        return ["INFO cultivation axis: folder cultivation/ not present yet (0 files; nothing to validate)"]
    out = [f"INFO cultivation axis: files read {len(C.loaded_files)}   disciplines with files {len(C.files_by_aff)}/{len(C.codes)}   "
           f"manuals: {len(C.manuals)}   moves: {len(C.moves)}   kingdom rows: {len(C.kingdom_rows)}   kit rows: {len(C.kits)}   "
           f"characters-ext rows: {len(C.chars_ext)}",
           f"INFO cultivation stock files absent: {C.absent['manuals']} manuals files, {C.absent['moves']} moves files "
           f"(of {len(C.codes) * len(GRADE_CODES)} each expected)"]
    for rel in ("affinities.csv", "kingdoms/azorion.csv", "kingdoms/gale.csv", "kits.csv", "characters-ext.csv"):
        if not C.file_exists(crel(*rel.split("/"))):
            out.append(f"INFO cultivation file absent: {crel(*rel.split('/'))}")
    return out


def cmd_affinity(C, code):
    code = code.upper()
    if code not in C.codes:
        print(f"error: {code!r} is not one of the {len(C.codes)} cultivation disciplines "
              f"({' '.join(C.codes)})", file=sys.stderr)
        return 2
    r = C.aff.get(code)
    if r:
        print(f"Discipline {code}  [{r['_file']}:{r['_line']}]")
        print_row(r)
    else:
        print(f"Discipline {code}: no affinities.csv row yet; design class {AFF_CLASS[code]}, req_kind {AFF_KIND[code]}")
    counts, src = C.counts(code)
    print(f"  counts source: {src}")
    if counts is None:
        return 0
    print("  grade  files(m/v)  manuals present/expected  moves present")
    tm = te = tv = 0
    for g in GRADE_CODES:
        folder = CODE_TO_FOLDER[g]
        mt = C.tables.get(crel("manuals", folder, f"{code}.csv"))
        vt = C.tables.get(crel("moves", folder, f"{code}.csv"))
        exp = cult_grade_rows(counts, g)
        pm = len(mt.rows) if mt and mt.exists and not mt.bad_header else 0
        pv = len(vt.rows) if vt and vt.exists and not vt.bad_header else 0
        files = f"{'Y' if mt and mt.exists else '-'}/{'Y' if vt and vt.exists else '-'}"
        print(f"  {g}    {files:<10}  {pm:>3}/{exp:<3}                   {pv}")
        tm += pm
        te += exp
        tv += pv
    print(f"  total manuals {tm}/{te}   moves {tv}")
    return 0


def cult_stats(C):
    print()
    print("== cultivation axis ==")
    if not C.present:
        print("INFO cultivation/ folder not present yet")
        return
    print(f"disciplines: {len(C.codes)}   affinities.csv rows: {len(C.aff)}")
    tp = te = 0
    for g in GRADE_CODES:
        folder = CODE_TO_FOLDER[g]
        present = exp = fp = mv = 0
        for a in C.codes:
            counts, _ = C.counts(a)
            exp += cult_grade_rows(counts, g) if counts else 0
            t = C.tables.get(crel("manuals", folder, f"{a}.csv"))
            if t and t.exists:
                fp += 1
                present += len(t.rows) if not t.bad_header else 0
            vt = C.tables.get(crel("moves", folder, f"{a}.csv"))
            if vt and vt.exists and not vt.bad_header:
                mv += len(vt.rows)
        tp += present
        te += exp
        print(f"  {g}: manuals {present}/{exp}  files {fp}/{len(C.codes)}  moves {mv}")
    print(f"  total cultivation manuals {tp}/{te}")
    pers = sorted(rel for rel in C.tables if "/personal/" in rel and rel.endswith("-manuals.csv") and C.tables[rel].exists)
    print(f"kingdom rows: azorion {len(C.tables[crel('kingdoms', 'azorion.csv')].rows) if C.file_exists(crel('kingdoms', 'azorion.csv')) else 'file absent'}, "
          f"gale {len(C.tables[crel('kingdoms', 'gale.csv')].rows) if C.file_exists(crel('kingdoms', 'gale.csv')) else 'file absent'}")
    print(f"personal files: {len(pers)} manual files; kit rows {len(C.kits)}; characters-ext rows {len(C.chars_ext)}")
    print(f"total cultivation moves read: {len(C.moves)}   manuals read: {len(C.manuals)}")
    print(f"not yet generated: manual files absent {C.absent['manuals']}, moves files absent {C.absent['moves']}")


def cmd_usable_cult(root, code):
    """Section 10 of the design: cultivation Usable / Latent for a character, from kits.csv and characters-ext.csv."""
    C = CultLedger(root)
    ch, _ = load_char(root, code)
    if ch is None:
        return 2
    cid = ch["char_id"]
    print()
    print(f"Cultivation usable report for {cid} - {ch['name']}")
    kt = C.tables.get(crel("kits.csv"))
    if not kt or not kt.exists:
        print("  cultivation/kits.csv does not exist yet")
        return 0
    rows = [r for r in C.kits if r["char_id"] == cid]
    if not rows:
        print("  no cultivation kit rows")
        return 0
    eff = ch["effective_realm"]
    ag = access_group(eff)
    epos = realm_pos(eff)
    cap = realm_affinity_cap(eff)
    ext = C.chars_ext.get(cid, {})
    blocked_types = {TYPE_BY_CODE[b] for b in split_codes(ch["blocked_types"]) if b in TYPE_BY_CODE}
    aff = parse_affinity(ch["affinity"])
    floor_ok = bool(epos and epos >= realm_pos(CFLOOR))
    print(f"  effective_realm {eff} (AG{ag}); cultivation floor {'met' if floor_ok else 'NOT met: every move is Latent'}")
    totals = {"Usable": 0, "Conditional": 0, "Latent": 0}
    for kr in rows:
        mid = kr["manual_id"]
        man = C.manuals.get(mid)
        if man is None:
            print(f"  {mid}: manual row not found (file not yet generated?)")
            continue
        a = man["affinity_id"]
        kind = C.req_kind(a)
        req = man["affinity_req"]
        gate_ok, why_gate = True, "no discipline gate"
        if kind == "A" and re.fullmatch(r"A[2-7]", req):
            nm = (C.aff.get(a) or {}).get("name", "")
            lvls = [min(l, cap or 0) for t, l in aff if nm and (t.lower() in nm.lower() or nm.lower() in t.lower())]
            best = max(lvls, default=0)
            gate_ok = best >= int(req[1:])
            why_gate = f"{req}: best usable level {best} (cap {cap})"
        elif kind == "SR" and req in SR_CODES:
            sr = ext.get("soul_rung", "")
            m = re.search(r"(\d+)", sr)
            gate_ok = bool(m and int(m.group(1)) >= int(req[2:]))
            why_gate = f"{req} vs soul_rung {sr or 'none'}"
        elif kind == "HL" and req in HL_CODES:
            hl = ext.get("heart_level", "")
            m = re.search(r"(\d+)", hl)
            gate_ok = bool(m and int(m.group(1)) >= int(req[2:]))
            why_gate = f"{req} vs heart_level {hl or 'none'}"
        print(f"  {mid}  {man['title']}  ({man['grade']}, {man['realm_band']}; {why_gate})")
        counts = {"Usable": 0, "Conditional": 0, "Latent": 0}
        for m in sorted(C.moves_by_manual.get(mid, []), key=lambda m: m["seq"]):
            typ = m["move_type"]
            if typ not in ACCESS_MATRIX or ag is None:
                continue
            cell = ACCESS_MATRIX[typ][ag - 1]
            state = "Usable" if cell in ("S", "P") else "Conditional" if cell == "R" else "Latent"
            note = f"cell {cell}"
            if not floor_ok:
                state, note = "Latent", note + ", below floor"
            elif not gate_ok:
                state, note = "Latent", note + ", discipline gate not met"
            if typ in blocked_types:
                state, note = "Latent", note + ", blocked by seal"
            counts[state] += 1
            totals[state] += 1
            print(f"    {m['seq']} {m['move_id']}  {m['name']}  [{typ}]  {state}  ({note})")
        print(f"    -> Usable {counts['Usable']}, Conditional {counts['Conditional']}, Latent {counts['Latent']}")
    print(f"  Totals over {len(rows)} cultivation manuals: Usable {totals['Usable']}, Conditional {totals['Conditional']}, Latent {totals['Latent']}")
    return 0


# ---------------------------------------------------------------------------------------------------------------
# Query commands
# ---------------------------------------------------------------------------------------------------------------

def print_row(r, cols=None, indent="  "):
    cols = cols or [k for k in r if not k.startswith("_")]
    w = max(len(c) for c in cols)
    for c in cols:
        print(f"{indent}{c.ljust(w)} : {r.get(c, '')}")


def resolve_manual(root, mid):
    """Return (manual_row, info, table) for a MAN-/PER-/FND- ID, or (None, info, table)."""
    info = parse_id(mid)
    if info is None or info.kind not in ("manual", "personal", "found"):
        return None, info, None
    t = read_table(root, info.rel_file)
    rows = [r for r in t.rows if r.get("manual_id") == mid]
    return (rows[0] if rows else None), info, t


def cmd_manual(root, ident):
    info = parse_id(ident)
    if info is None:
        print(f"error: {ident!r} matches no ID scheme (MAN-, AZ-, GA-, PER-, FND-, CMAN-, CAZ-, CGA-, PCM-)", file=sys.stderr)
        return 2
    if info.kind in ("move", "personal_move", "found_move"):
        print(f"error: {ident} is a move ID; use  moves {ident}", file=sys.stderr)
        return 2
    kr = None
    gen = ident
    if info.kind == "kingdom":
        t = read_table(root, info.rel_file)
        hits = [r for r in t.rows if r.get("kingdom_id") == ident]
        if not hits:
            print(f"not found: {ident} (looked in {info.rel_file}{'' if t.exists else ', file does not exist yet'})", file=sys.stderr)
            return 2
        kr = hits[0]
        print(f"Kingdom row {ident}  [{info.rel_file}:{kr['_line']}]")
        print_row(kr)
        gen = kr["manual_id"]
        print()
    man, ginfo, _ = resolve_manual(root, gen)
    if man is None:
        print(f"not found: {gen} (looked in {ginfo.rel_file if ginfo else '?'})", file=sys.stderr)
        return 2
    print(f"Manual {gen}  [{man['_file']}:{man['_line']}]")
    print_row(man)
    mrel = manual_moves_file(ginfo)
    mt = read_table(root, mrel)
    n = len([r for r in mt.rows if r.get("manual_id") == gen])
    print(f"  move rows : {n}  (in {mrel}{'' if mt.exists else ', file does not exist yet'})")
    if ginfo.kind == "manual":
        cult = ginfo.axis == "cultivation"
        for kf, label in ((("azorion", "CAZ"), ("gale", "CGA")) if cult else
                          (("azorion", "AZ"), ("gale", "GA"), ("brackenhold", "BR"))):
            kt = read_table(root, (f"{AXIS_DIR}/" if cult else "") + f"kingdoms/{kf}.csv")
            rows = [r for r in kt.rows if r.get("manual_id") == gen]
            if not kt.exists:
                print(f"  kingdom {label}: {kt.rel} does not exist yet")
            for r in rows:
                if kr is not None and r["kingdom_id"] == ident:
                    continue
                print(f"  kingdom row {r['kingdom_id']} [{r['_file']}:{r['_line']}]: {r['institution']} | "
                      f"channel {r['channel']} | access {r['access']} | copy {r['copy_control']} | status {r['status']}")
                if r["local_note"]:
                    print(f"      local_note: {r['local_note']}")
    return 0


def cmd_moves(root, ident):
    info = parse_id(ident)
    if info is None:
        print(f"error: {ident!r} matches no ID scheme", file=sys.stderr)
        return 2
    if info.kind == "kingdom":
        ident = info.manual_id
        info = parse_id(ident)
    if info.kind in ("move", "personal_move", "found_move"):
        t = read_table(root, info.rel_file)
        hits = [r for r in t.rows if r.get("move_id") == ident]
        if not hits:
            print(f"not found: {ident} (looked in {info.rel_file}{'' if t.exists else ', file does not exist yet'})", file=sys.stderr)
            return 2
        r = hits[0]
        print(f"Move {ident}  [{r['_file']}:{r['_line']}]")
        print_row(r)
        return 0
    rel = manual_moves_file(info)
    t = read_table(root, rel)
    rows = sorted([r for r in t.rows if r.get("manual_id") == ident], key=lambda r: r["seq"])
    if not rows:
        print(f"not found: no move rows for {ident} in {rel}{'' if t.exists else ' (file does not exist yet)'}", file=sys.stderr)
        return 2
    man, _, _ = resolve_manual(root, ident)
    head = f"Moves of {ident}"
    if man:
        head += f" - {man['title']} ({man['grade']}, {man['realm_band']}, min {man['min_realm']}, {man['composition']})"
    print(head)
    for r in rows:
        print(f"  {r['seq']} {r['move_id']}  {r['name']}  [{r['move_type']} | {r['function']} | {r['form']} | {r['cost_class']} | {r['status']}]")
        print(f"       {r['description']}")
    print(f"  {len(rows)} move rows  [{rel}]")
    return 0


def load_char(root, code):
    t = read_table(root, "characters.csv")
    if not t.exists:
        print("error: characters.csv does not exist yet", file=sys.stderr)
        return None, None
    hits = [r for r in t.rows if r["char_id"].upper() == code.upper()]
    if not hits:
        print(f"error: character {code!r} not in characters.csv (known: {', '.join(r['char_id'] for r in t.rows)})", file=sys.stderr)
        return None, None
    return hits[0], t


def kit_rows(root, cid):
    t = read_table(root, "character-kits.csv")
    return t, [r for r in t.rows if r["char_id"] == cid]


def cmd_kit(root, code):
    ch, _ = load_char(root, code)
    if ch is None:
        return 2
    cid = ch["char_id"]
    print(f"Kit of {cid} - {ch['name']} (tier {ch['tier']}, {ch['kingdom']}); realm {ch['realm']}, effective {ch['effective_realm']}, "
          f"blocked {ch['blocked_types']}")
    kt, rows = kit_rows(root, cid)
    if not kt.exists:
        print("  character-kits.csv does not exist yet")
        return 0
    if not rows:
        print("  no kit rows")
        return 0
    for r in rows:
        man, info, _ = resolve_manual(root, r["manual_id"])
        if man:
            desc = f"{man['title']} | {man['grade']} | {man['realm_band']} | min {man['min_realm']} | {man['move_count']} moves | {man['weapon_id']}"
        else:
            desc = "(manual row not found: file may not be generated yet)"
        print(f"  {r['manual_id']}  {desc}")
        print(f"      via {r['kingdom_manual_id'] or '-'} | source {r['source']} | {r['learned_via']} | mastery {r['mastery']} | {r['assign_status']}"
              + (f" | note {r['note']}" if r["note"] else ""))
    print(f"  {len(rows)} kit rows")
    return 0


def parse_affinity(cell):
    out = []
    for a in split_codes(cell):
        if ":" in a:
            typ, lvl = a.split(":", 1)
            out.append((typ.strip(), AFFINITY_LEVELS.get(lvl.strip(), 0)))
    return out


def realm_affinity_cap(eff):
    n = realm_name(eff)
    if n is None:
        return None
    i = REALM_INDEX[n]
    if i == 0:
        return 1
    if i <= 5:
        return 3
    if i <= 9:
        return 5
    if i <= 11:
        return 6
    return 8


def aligned_force(weapon_row):
    if not weapon_row:
        return None
    if weapon_row["family"] in SWORD_FAMILIES or weapon_row["weapon_id"] in SWORD_CODES_EXTRA:
        return "Swords"
    if weapon_row["family"] == UNARMED_FAMILY:
        return "Strength"
    return None


def eligibility(root, ch, man, kit, weapons, grade_hold):
    """Rule 42.11.6.1, informational. Returns list of (label, verdict, detail)."""
    out = []
    eff = ch["effective_realm"]
    ag = access_group(eff)
    epos = realm_pos(eff)
    mpos = realm_pos(man["min_realm"])
    if epos and mpos:
        out.append(("realm", "met" if epos >= mpos else "NOT met", f"effective {eff} vs min_realm {man['min_realm']}"))
    e = man["energy_req"]
    if e in ENERGY_LADDER and ag:
        hi = AG_HIGHEST_ENERGY[ag]
        out.append(("energy", "met" if ENERGY_LADDER.index(e) <= ENERGY_LADDER.index(hi) else "NOT met", f"{e} vs highest {hi} for AG{ag}"))
    cparts = man["cultivation_req"].split("+")
    st = cparts[0]
    rn = realm_name(eff)
    if st in CULT_STATES and rn:
        ri = REALM_INDEX[rn]
        if st == "NONE":
            ok = True
        elif st.startswith("T1-"):
            stage = st[3:].capitalize()
            ok = ri > 0 or (T1_STAGES.index(stage) <= epos[1] if stage in T1_STAGES else False)
        else:
            need = {"CIRC": 1, "MER-PART": 1, "MER-FULL": 3, "MER-NET": 5, "XT-FIELD": 6, "CORE-ON": 10, "DIVINE": 13}[st]
            ok = ri >= need
        out.append(("cultivation state", "met" if ok else "NOT met", f"{st} at {eff}"))
    for lk in cparts[1:]:
        if lk == "LINK-PRIOR":
            out.append(("link LINK-PRIOR", *link_prior(root, ch["char_id"], man, grade_hold)))
        else:
            out.append((f"link {lk}", "not evaluated", "needs the character's Named Moves or ledger"))
    aff = parse_affinity(ch["affinity"])
    cap = realm_affinity_cap(eff)
    a = man["affinity_req"]
    if cap is not None and (a in AFFINITY_CODES or a == "A4+A4" or (a.endswith("W") and a[:-1] in AFFINITY_CODES)):
        eff_levels = [(t, min(l, cap)) for t, l in aff]
        if a == "NONE":
            out.append(("affinity", "met", "NONE"))
        elif a == "A4+A4":
            n = len([1 for _, l in eff_levels if l >= 4])
            out.append(("affinity", "met" if n >= 2 else "NOT met", f"A4+A4: {n} affinities at Level 4+ (cap {cap})"))
        else:
            weapon_aligned = a.endswith("W")
            lvl = int((a[:-1] if weapon_aligned else a)[1:])
            pool = eff_levels
            if weapon_aligned:
                force = aligned_force(weapons.get(man["weapon_id"]))
                pool = [(t, l) for t, l in eff_levels if force and t.lower() == force.lower()]
            best = max([l for _, l in pool], default=0)
            out.append(("affinity", "met" if best >= lvl else "NOT met", f"{a}: best usable level {best} (realm cap {cap})"))
    sv = ch["sovereignty"]
    s = man["sovereignty_req"]
    if s in SOV_CODES:
        if s == "NONE":
            ok = True
        elif s == "SOV-C":
            ok = sv != "none"
        elif s == "SOV-CW":
            f = aligned_force(weapons.get(man["weapon_id"]))
            ok = sv.startswith("ceiling:") and bool(f) and sv.split(":", 1)[1].lower() == f.lower()
        elif s == "SOV-H":
            ok = sv.startswith("held:")
        else:
            ok = sv.startswith("origin:")
        out.append(("sovereignty", "met" if ok else "NOT met", f"{s} vs {sv}"))
    out.append(("access", "not evaluated", "standing at the institution is not stored in the ledger"))
    return out


def link_prior(root, cid, man, held):
    """LINK-PRIOR: the character holds a manual of the same weapon, next lower grade (any lower for FUS/CAT/MYT) at Practiced+."""
    g = man["grade"]
    if g not in GRADE_CODES:
        return ("not evaluated", "unknown grade")
    gi = GRADE_CODES.index(g)
    if g in ("BAS",):
        return ("met", "Basic has no prior grade")
    wanted = GRADE_CODES[gi - 1:gi] if g not in ("FUS", "CAT", "MYT") else GRADE_CODES[:gi]
    for hm, kitrow in held:
        if hm and hm["weapon_id"] == man["weapon_id"] and hm["grade"] in wanted and \
                MASTERY.index(kitrow["mastery"]) >= 1 if hm and kitrow["mastery"] in MASTERY else False:
            return ("met", f"holds {hm['manual_id']} ({hm['grade']}) at {kitrow['mastery']}")
    return ("NOT met", f"no kit manual of weapon {man['weapon_id']} in grade {'/'.join(wanted)} at Practiced or better")


def cmd_usable(root, code):
    ch, _ = load_char(root, code)
    if ch is None:
        return 2
    cid = ch["char_id"]
    eff = ch["effective_realm"]
    ag = access_group(eff)
    if ag is None:
        print(f"error: effective_realm {eff!r} of {cid} does not parse; run validate", file=sys.stderr)
        return 2
    blocked = [b for b in split_codes(ch["blocked_types"])]
    blocked_types = {TYPE_BY_CODE[b] for b in blocked if b in TYPE_BY_CODE}
    print(f"Usable report for {cid} - {ch['name']}")
    print(f"  realm {ch['realm']}; effective_realm {eff} -> access group AG{ag}; blocked_types {ch['blocked_types']}")
    wt = read_table(root, "weapons.csv")
    weapons = {r["weapon_id"]: r for r in wt.rows}
    kt, rows = kit_rows(root, cid)
    if not kt.exists:
        print("  character-kits.csv does not exist yet")
        return 0
    if not rows:
        print("  no kit rows: nothing to compute")
        return 0
    held = []
    for r in rows:
        man, _, _ = resolve_manual(root, r["manual_id"])
        held.append((man, r))
    totals = {"Usable": 0, "Conditional": 0, "Latent": 0}
    for man, kitrow in held:
        mid = kitrow["manual_id"]
        print()
        if man is None:
            print(f"{mid}: manual row not found (file not yet generated?)")
            continue
        info = parse_id(mid)
        mt = read_table(root, manual_moves_file(info))
        moves = sorted([m for m in mt.rows if m.get("manual_id") == mid], key=lambda m: m["seq"])
        print(f"{mid}  {man['title']}  ({man['grade']}, {man['realm_band']}, {man['composition']}, "
              f"mastery {kitrow['mastery']}, {kitrow['assign_status']})")
        conds_met = {tok[5:] for tok in split_codes(kitrow["note"]) if tok.startswith("COND:")}
        if not moves:
            print("  no move rows found (file not yet generated?)")
            continue
        counts = {"Usable": 0, "Conditional": 0, "Latent": 0}
        for m in moves:
            typ = m["move_type"]
            if typ not in ACCESS_MATRIX:
                print(f"  {m['seq']} {m['name']}: unknown move_type {typ!r}")
                continue
            cell = ACCESS_MATRIX[typ][ag - 1]
            why = f"cell {cell}"
            cond = ""
            if cell in ("S", "P"):
                state = "Usable"
            elif cell == "R":
                state = "Conditional"
                cond = COND_CODE.get((typ, ag), "?")
                why += f", condition {cond}"
            else:
                state = "Latent"
            if typ in blocked_types:
                state = "Latent"
                why += ", blocked by seal"
            if state == "Conditional" and cond in conds_met:
                state = "Usable"
                why += " (COND token recorded in kit note)"
            elif state == "Conditional":
                why += " (COND token not recorded: not available)"
            counts[state] += 1
            totals[state] += 1
            print(f"  {m['seq']} {m['move_id']}  {m['name']}  [{typ}]  {state}  ({why}; AG{ag} {typ})")
        print(f"  -> Usable {counts['Usable']}, Conditional {counts['Conditional']}, Latent {counts['Latent']}")
        print("  eligibility (informational, Rule 42.11.6.1):")
        for label, verdict, detail in eligibility(root, ch, man, kitrow, weapons, held):
            print(f"    {label}: {verdict} - {detail}")
    print()
    print(f"Totals over {len(rows)} manuals: Usable {totals['Usable']}, Conditional {totals['Conditional']}, Latent {totals['Latent']}")
    return 0


def cmd_find_name(L, text, C=None, axis="both"):
    q = compare_form(text)
    if not q:
        print("error: empty search text", file=sys.stderr)
        return 2
    qt = set(q.split())
    hits = []

    def consider(kind, idv, label, r):
        f = compare_form(label)
        if not f:
            return
        if f == q:
            hits.append((0, "EXACT", kind, idv, label, r, 1.0))
            return
        ft = set(f.split())
        if qt == ft and len(qt) > 1:
            hits.append((1, "NEAR (same words, other order)", kind, idv, label, r, 1.0))
            return
        # short names: similarity alone is too loose; ask for a higher ratio and a similar length
        ratio = difflib.SequenceMatcher(None, q, f).ratio()
        short = min(len(q), len(f)) < 10
        need = 0.93 if short else 0.85
        if ratio >= need and abs(len(q) - len(f)) <= max(2, len(q) // 4):
            hits.append((2, f"NEAR (similarity {ratio:.2f})", kind, idv, label, r, ratio))
        elif len(qt) >= 2 and (qt <= ft or ft <= qt) and min(len(qt), len(ft)) >= 2:
            hits.append((3, "NEAR (one name holds all the words of the other)", kind, idv, label, r, 0.0))

    wmoves, wmans = (L.moves, L.manuals) if axis in ("weapon", "both") else ({}, {})
    cmoves, cmans = (C.moves, C.manuals) if (C is not None and axis in ("cultivation", "both")) else ({}, {})
    for mvid, r in list(wmoves.items()) + list(cmoves.items()):
        consider("move", mvid, r["name"], r)
    for mid, r in list(wmans.items()) + list(cmans.items()):
        consider("manual", mid, r["title"], r)
    for i in INSTITUTIONS:
        f = compare_form(i)
        if f == q:
            hits.append((0, "EXACT", "institution", "-", i, None, 1.0))
    # exact hits first, then near hits by tier and falling similarity
    hits.sort(key=lambda h: (h[0], -h[6], h[3]))
    scanned = f"{len(wmoves)} moves, {len(wmans)} manuals scanned"
    if C is not None and axis in ("cultivation", "both"):
        scanned += f"; cultivation axis: {len(cmoves)} moves, {len(cmans)} manuals scanned"
    print(f"find-name {text!r}  (comparison form {q!r}; {scanned})")
    if not hits:
        print("  no equal or close name found")
        return 0
    shown = hits[:40]
    for _, how, kind, idv, label, r, _ratio in shown:
        where = f" [{r['_file']}:{r['_line']}]" if r else ""
        print(f"  {how}: {kind} {idv}  {label!r}{where}")
    if len(hits) > len(shown):
        print(f"  ... {len(hits) - len(shown)} more near hits not shown (exact hits always sort first)")
    print(f"  {len(hits)} hit(s); {len([h for h in hits if h[1] == 'EXACT'])} exact")
    return 0


def cmd_stats(L, C=None, axis="both"):
    root = L.root
    print(f"Manual Ledger stats - {root}")
    print(f"weapon types in weapons.csv: {len(L.weapons)}")
    print()
    print("generic manuals by grade (rows present / rows weapons.csv expects)  |  files present / expected")
    tot_present = tot_exp = 0
    for g in GRADE_CODES:
        folder = CODE_TO_FOLDER[g]
        present = exp = fp = fe = mp = 0
        mv = 0
        for w in L.weapon_order:
            e = (expected_rows(g, L.weapons[w]) or 0) + bh_extra(L, g, w)
            exp += e
            t = L.tables.get(f"manuals/{folder}/{w}.csv")
            fe += 1
            if t and t.exists:
                fp += 1
                present += len(t.rows) if not t.bad_header else 0
            vt = L.tables.get(f"moves/{folder}/{w}.csv")
            if vt and vt.exists and not vt.bad_header:
                mv += len(vt.rows)
        tot_present += present
        tot_exp += exp
        note = "  (header-only grade; expected empty)" if g in HEADER_ONLY_GRADES else ""
        print(f"  {g}: manuals {present}/{exp}  files {fp}/{fe}  moves {mv}{note}")
    print(f"  total generic manuals {tot_present}/{tot_exp}")
    print()
    print(f"kingdom rows: azorion {len(L.tables['kingdoms/azorion.csv'].rows) if L.file_exists('kingdoms/azorion.csv') else 'file absent'}, "
          f"gale {len(L.tables['kingdoms/gale.csv'].rows) if L.file_exists('kingdoms/gale.csv') else 'file absent'}, "
          f"brackenhold {len(L.tables['kingdoms/brackenhold.csv'].rows) if L.file_exists('kingdoms/brackenhold.csv') else 'file absent'}")
    pers = sorted(rel for rel in L.tables if rel.startswith("personal/") and rel.endswith("-manuals.csv") and L.tables[rel].exists)
    pm = sum(len(L.tables[r].rows) for r in pers)
    pmv = sum(len(t.rows) for rel, t in L.tables.items() if rel.startswith("personal/") and rel.endswith("-moves.csv") and t.exists)
    print(f"personal files: {len(pers)} manual files, {pm} personal manuals, {pmv} personal moves")
    print(f"characters: {len(L.chars)}   kit rows: {len(L.kits)}")
    print(f"total moves read: {len(L.moves)}   total manuals read (all kinds): {len(L.manuals)}")
    print()
    print("not yet generated:")
    print(f"  stock manual files absent: {len(L.missing['manuals'])}   stock move files absent: {len(L.missing['moves'])}")
    print(f"  header-only files absent (fusion/catastrophic/mythic): manuals {len(L.missing['header-only manuals'])}, "
          f"moves {len(L.missing['header-only moves'])}")
    print(f"  kingdom files absent: {', '.join(L.missing['kingdoms']) or 'none'}")
    print(f"  characters.csv absent: {L.missing['characters']}   character-kits.csv absent: {L.missing['character-kits']}")
    if C is not None and axis in ("cultivation", "both"):
        cult_stats(C)
    return 0


# ---------------------------------------------------------------------------------------------------------------

def default_root():
    # <repo>/.claude/tools/manual_ledger_query.py -> <repo>/.claude/story-memory/ledger-manuals
    return Path(__file__).resolve().parent.parent / "story-memory" / "ledger-manuals"


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="Read-only Manual Ledger query and validation tool (Part 42). Writes nothing.")
    ap.add_argument("--root", help="ledger-manuals folder (default: the repo's .claude/story-memory/ledger-manuals)")
    ap.add_argument("--axis", choices=("weapon", "cultivation", "both"), default="both",
                    help="which axis validate, stats, find-name and usable cover (default both)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, arg, hlp in (("manual", "ID", "manual row of a MAN-, AZ-, GA-, PER- or FND- ID"),
                           ("moves", "ID", "moves of a manual ID, or one move ID"),
                           ("kit", "CHARACTER", "kit rows of a character (char_id)"),
                           ("usable", "CHARACTER", "Usable/Conditional/Latent report for a character"),
                           ("find-name", "TEXT", "moves and manuals whose name equals or closely matches TEXT"),
                           ("name", "TEXT", "alias of find-name (Rule 42.10.9.2)")):
        p = sub.add_parser(name, help=hlp)
        p.add_argument(arg.lower(), metavar=arg)
        p.add_argument("--axis", choices=("weapon", "cultivation", "both"), default=argparse.SUPPRESS)
    p = sub.add_parser("affinity", help="a cultivation discipline: row, expected and present counts by grade")
    p.add_argument("code", metavar="CODE")
    for name, hlp in (("validate", "run ledger checks, exit 1 on any FAIL"),
                      ("stats", "counts of what exists and what is not yet generated")):
        p = sub.add_parser(name, help=hlp)
        p.add_argument("--axis", choices=("weapon", "cultivation", "both"), default=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    root = Path(args.root).resolve() if args.root else default_root()
    if not root.is_dir():
        print(f"error: ledger folder not found: {root}", file=sys.stderr)
        return 2
    c = args.cmd
    if c == "manual":
        return cmd_manual(root, args.id)
    if c == "moves":
        return cmd_moves(root, args.id)
    if c == "kit":
        return cmd_kit(root, args.character)
    if c == "usable":
        if args.axis in ("weapon", "both"):
            rc = cmd_usable(root, args.character)
            if rc != 0:
                return rc
        if args.axis in ("cultivation", "both"):
            return cmd_usable_cult(root, args.character)
        return 0
    if c == "affinity":
        return cmd_affinity(CultLedger(root), args.code)
    if c in ("find-name", "name"):
        return cmd_find_name(Ledger(root), args.text, CultLedger(root), args.axis)
    if c == "validate":
        return cmd_validate(Ledger(root), CultLedger(root), args.axis)
    if c == "stats":
        return cmd_stats(Ledger(root), CultLedger(root), args.axis)
    return 2


if __name__ == "__main__":
    sys.exit(main())
