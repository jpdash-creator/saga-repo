---
description: Preview the current Chapter's written Areas assembled together, without exporting a final file.
user-invocable: true
---

# `/preview-chapter`

Corresponds to canon command `[PREVIEW CHAPTER]` (C-31). Read-only — assembles the current
Chapter's already-written Areas (`chapter-NNN/area-NN.md`) in order for review (never the `_archive` folder), without writing/concatenating the
Chapter's per-Area files into an output document (see `/chapter-builder` for the condensed Chapter file).
The Areas are shown as the reader will see them: each Area under its Area Title Block (icon, title
and reference code) and its date line, in Area order, as the Areas stand in their per-Area files (the Chapter file made by `/chapter-builder` has no Area Title Blocks). If an Area file lacks its title block,
name the file and show it as written. A Chapter built whole by `/create-chapter` has no Area files: the preview then shows the written Chapter
file (`Chapter NNN - <Name>.md` in the Novel-Part folder) as it stands, with its hidden `<!-- AREA NN -->`
markers shown as small `Area NN` labels so the joins can be read, and reports the Chapter-level word count
against its band; there is no Area list. The preview ends by noting whether the Chapter is still open
(an Area row of the Chapter Spec is not yet `WRITTEN` or `DROPPED`; this is the Area row status, not the spec status).
