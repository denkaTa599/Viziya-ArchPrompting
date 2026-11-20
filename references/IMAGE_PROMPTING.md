# Image prompting — core workflow

Version 1.0. The router in `../SKILL.md` determines which specialist references are loaded. This core is mandatory for prompt work and image analysis; do not silently expand every prompt with specialist checklists.

## Model selection

Use the user's explicit **Nano Banana**, **GPT Image**, or **ChatGPT Images** choice immediately, without confirmation. GPT Image and ChatGPT Images are the same family here. Otherwise inherit the established model until the user changes it; a named new model overrides the previous selection.

Ask which family to use, in the user's language, only when no model is established and its selection affects the requested prompt format or correction. Wait for that essential answer before delivering model-specific blocks. Model-neutral visual analysis/comparison can proceed without choosing a model. Skill discussion and maintenance never trigger a model-selection question. Do not invent a model version or unsupported API controls.

## Establish task and evidence

1. Identify new generation, transformation of a base, local edit, diagnosis, or comparison.
2. Inspect images actually available; distinguish observed attributes, user-defined facts, unknowns and assumptions. Never describe unseen references.
3. Assign the fewest necessary, numbered reference roles and priority by property: **base** = geometry/camera/layout; **material/light/style** = only the named surface or visual treatment; **identity/product** = recognizable distinctive features. Do not import other properties from a secondary reference.
4. Record **fixed properties**, **permitted changes**, and physical consequences (e.g. a new light source legitimately changes shadows; new cladding changes reflections).
5. Build: goal/output, reference roles, subject and action, composition, materials/light, edit scope, literal text if any, and delivery. Include counts, location, crop, aspect ratio and visual hierarchy only where relevant.

Use positive, concrete visual language; minimal task-relevant exclusions. Do not add people, cars, vegetation, signs or architecture without user approval. Do not use generic superlatives as substitutes for material/camera/lighting specification. Keep existing global exposure, white balance and outside regions stable for truly local edits; for full photographic conversion allow the requested global changes.

## Camera / fidelity / photos

Preserve observable camera anchors such as roof-line placement, horizon, field-of-view clues and frame-edge cuts when the source is authoritative. Only use a camera height when grounded; label estimated values as estimates. A focal-length cue is an *optional proposal* for photographic views (e.g. 24–28 mm interior, ~35 mm contextual exterior, 50–85 mm detail, full-frame equivalents); it may not override a fixed reference camera. Aperture/ISO are optional stylistic cues, not physical controls of the model. Avoid unverified model parameters. Offer optional people, 8K delivery/upscale, or Nano Banana fixed sampling temperature only when useful, supported and approved; do not presume support. Separately specify lighting color temperature in kelvin when relevant.

## Architecture — core safeguards

The current Revit/D5/3D view controls its own geometry and perspective. An approved prior photorealistic render may control assigned appearance, not a different shot's layout. Keep opening, mullion, balcony, roof and level geometry legible. Camera changes require explicit permission; new viewpoint is best based on a fresh model view. For detail shots use a suitable crop; never invent unseen geometry. Technical plans must retain linework/dimensions as separate accurate overlays if exactness matters. Describe material mapping as **element/zone → material → color → finish**. Specialist details live in architectural/material references.

## Model-specific prompt packaging

### Nano Banana

Return **two complete copyable blocks**, even for a correction: **System Instruction** (stable project or series rules, geometry/identity precedence, material map and permitted transformation) and **Prompt** (the specific action, numbered references, visual treatment and deliverable). Do not redundantly repeat everything across them; repeat only critical constraints. For a new chat, make both blocks self-contained. If no system field exists, advise concatenating them into a single user message with labeled sections. A failed output must not automatically become the new geometry anchor.

### ChatGPT Images / GPT Image

Return **one complete self-contained Prompt** containing target/base, reference roles, the action, locked properties, permitted physical changes and deliverable. Limit local edits to coherent regions. When image drift accumulates, use the original base/last approved frame; exact pixel preservation may require masks/compositing rather than text promises.

## Exact text / diagrams / special cases

For literal text: quote exact copy, case, diacritics, punctuation, count, location and typography relationship. For replacements state old → new and what layout may change. For numeric/dimensioned drawings recommend editable text/vector overlays when correctness matters. Diagrams should specify nodes, links, arrows, legend, reading order and verified values; do not invent information. Real transparency requires alpha and verification; a drawn checkerboard is not alpha.

## Diagnosis and final QA

For critique, compare actual visible result with fixed requirements before judging aesthetic treatment. Only describe images actually supplied. After 2–3 repeated failures of the same type, revisit the base, masking, compositing or model limitations; adding bans is not a default remedy. Compare variants under matching input conditions. Distinguish documented capabilities from hypotheses and observed experiments. Prompt creation itself does not initiate image generation.

For model-specific API claims check official documentation as needed (not every turn):
- https://developers.openai.com/api/docs/guides/image-prompting
- https://developers.openai.com/api/docs/guides/image-generation
- https://ai.google.dev/gemini-api/docs/image-generation
