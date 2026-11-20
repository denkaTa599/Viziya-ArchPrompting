---
name: image-prompting
description: Write, revise, diagnose and compare prompts for ChatGPT Images and Nano Banana, especially geometry-faithful architecture, photorealistic materials, references and controlled editing. Produces copyable prompt text, not images unless separately requested.
---

# Image Prompting — task router

Version 1.0. This entry point is the **only routing authority**. For prompt work or image analysis, read `references/IMAGE_PROMPTING.md`, then **only** the specialist references triggered below. Paths are relative to this skill directory. Do not read all files by default or assume they load automatically. Reuse complete, current instructions already available in context. If a needed file is unavailable, report the limitation.

## 1. Route by intent, not by keywords alone

First identify the requested operation: **new-image prompt**, **image-edit prompt**, **prompt revision**, **visual analysis/comparison**, or **failed-generation correction**. A prompt revision alone is not a generation failure; routine internal checking is not a request for visual QA. Skill maintenance/discussion alone needs no prompt modules.

Then identify reference roles (geometry, material/style, identity, approved anchor) and the properties actually being changed or evaluated. Route on those requirements, including requirements inherited from the conversation; words inside poster text or incidental scenery do not activate modules. Resolve the model using the core guide; analysis without model-specific delivery can proceed without selecting one.

| Specialist reference | Read when | Do not read merely because |
|---|---|---|
| `references/ARCHITECTURAL_FIDELITY.md` | Architecture / built space must follow a supplied model, drawing, camera, plan, elevation, existing façade or spatial constraints; architecture-specific generation or correction needs dimensional/compositional fidelity. | A building is incidental background or architecture is only a word in edited text. Technical fidelity alone does not request photographic or material treatment. |
| `references/MATERIAL_REALISM.md` | User specifies or corrects materials, textures, surface finish, weathering, natural imperfections, physical material behavior; **or** architectural photorealism makes material appearance a principal goal. | Generic photorealism without meaningful material decisions; minor text/logo edit. |
| `references/PHOTOGRAPHIC_REALISM.md` | Photographic appearance, CGI-to-photo conversion, realistic lighting, camera treatment, atmosphere, or defects in those properties are central. | Exact text replacement, technical diagram, fixed camera preservation alone, or the mere existence of a photograph. |
| `references/REFERENCE_DECONSTRUCTION.md` | An image is supplied to *extract or transfer* lighting, palette, style, materials, composition, or photographic look, or to reverse-describe its visual features. | Image acts only as a fixed geometry/base, face/product identity anchor, or local editing target. |
| `references/VISUAL_QA.md` | User provides a generated result for evaluation, asks why a generation failed, wants a corrective prompt after a failure, or requests a structured comparison. | First-pass generation with no result to critique. |
| `references/PROJECT_CONTINUITY.md` | Consistency across multiple related images/views, repeated people/products/locations, or transfer of established project constants from an approved anchor. | A single image or ordinary follow-up/local revision, even with an identity reference, unless cross-image continuity is requested. |

Read the union of applicable files, each once; module cross-references are explanations, **not load commands or dependencies**. Re-route changed requirements on follow-up; load only missing/currently unavailable instructions. Keep the chosen model, approved facts and locked properties unless the user changes them. Under context pressure, retain output contracts, reference roles, geometry/identity and permitted changes; shorten optional detail rather than omit a required module or critical constraint. A complex task may legitimately need every specialist.

### Typical routing

- New Revit exterior → core + architectural fidelity + material realism + photographic realism **when realistic material appearance is requested**.
- Change stone cladding in a fixed view → core + architectural fidelity + material realism; add photographic realism only when lighting/photographic finish is requested or defective.
- Transfer lighting/color from a photo → core + reference deconstruction + photographic realism; add architecture when a building base must be preserved.
- Diagnose warped hotel façade → core + architectural fidelity + visual QA; add material/photographic modules only when those are also at issue.
- Consistent series of views → core + project continuity; add architecture/material/photographic modules for actual requirements of the views.
- Replace text in a poster → core only (unless results reveal a special need).

## 2. Global precedence and guardrails

1. Explicit user instructions and supplied authoritative geometry/identity/reference roles.
2. Approved project facts and locked properties; preserve their meaning across tasks.
3. Core model-specific delivery rules in `references/IMAGE_PROMPTING.md`.
4. Applicable specialist guidance; task-specific rules supersede optional general suggestions.
5. Stylistic defaults and examples (never mandatory by themselves).

If rules conflict, resolve in favor of the higher priority, omit unsupported assumptions, and avoid repeating contradictory demands. Never claim exact preservation is guaranteed by a generative image model. A screenshot cannot prove hidden dimensions or unseen façades. Do not invent reference images, viewing angles, texture parameters, tools, model controls, or output resolution. Physical material descriptions in prompts are *visual cues*, not actual PBR map editing.

## 3. Output contract

- **Nano Banana:** full **System Instruction** + **Prompt** (two copyable sections), also for correction requests. If the interface has no system field, say how to combine them.
- **ChatGPT Images / GPT Image:** one self-contained **Prompt**.
- Name attachment order and roles briefly when relevant; explain in the user's language, use English for model instructions unless requested otherwise.
- Prompt creation never authorizes image generation, file writing, external actions or publishing. Only perform those when explicitly requested.
- Keep outputs concise but complete; use specialists to improve decisions, **not** to paste every checklist into the prompt.
- Use an explicitly named model immediately; otherwise retain the established model. Ask only when unresolved selection affects the requested output, as detailed in the core guide. Skill discussion and model-neutral analysis do not require a selection question.

## 4. Final internal checklist

Check model-specific format, locked-vs-editable scope, geometry/identity, references and precedence, visibility at camera scale, materials where applicable, consistency between light and reflections, exact user text, and contradictions. If critical inputs are missing, ask only for essentials; otherwise proceed with grounded assumptions.
