# Visual QA — diagnose and correct image-generation failures

Load only if a rendered result is actually provided for critique/comparison or a failure/correction is requested. Never pretend to see an unavailable output. Distinguish observed defect, likely cause and proposed corrective action.

## Hierarchical assessment

1. **Critical fidelity:** intended identity, visible architecture, storey and opening counts, component placement, exact text/counts, cropped mandatory areas.
2. **Reference fidelity:** camera, viewpoint, assigned identity/product attributes, material mapping and approved series anchor.
3. **Physical plausibility:** light/shadows, reflections, textures, material-specific imperfections, perspective, object contact and scale.
4. **Aesthetic finish:** tone, color, depth of field, context, composition and editorial coherence.

An attractive render with altered façade geometry is a failure on an architectural fidelity task. Do not optimize aesthetics before the critical invariants.

## Diagnosis record (internal; present a compact explanation when useful)

- **Observed issue:** what visibly differs from the input/brief?
- **Constraint violated:** locked geometry, material, camera, identity or local edit scope?
- **Hypothesized cause:** competing references, ambiguous material mapping, excessively broad edit, missing view, model limitation; label hypotheses, not facts.
- **Correction class:** geometry / camera / material / illumination / context / text / identity / continuity.
- **Next prompt strategy:** limit change to the broken class, retain already approved geometry, camera, materials and treatment outside that correction, and include necessary physical consequences. A user-reported failure without a visible result remains reported evidence, not a visually verified finding.
- **New base:** original authoritative image or last *verified* acceptable result, not automatically the latest failed output.

## Corrective strategies

| Failure | First-line response | Escalation after repeated failure |
|---|---|---|
| Openings, fins, storeys or roof drift | Return to original geometric base; restate essential visible anchors and edit scope | Better native 3D view, local mask/compositing, manual geometry correction |
| Wrong angle/crop | Specify fixed camera anchors and frame edges; remove conflicting lens/angle cues | Re-export target camera from 3D authoring tool |
| Wrong material on one zone | Explicit zone → material → finish correction; keep unrelated regions fixed | Crop/mask affected zone or simplify style references |
| Plastic or dirty surfaces | Correct material optical behavior, age and imperfection scale | Use close material reference or revise source render textures |
| Unrealistic light | Choose coherent lighting source and realistic reflection response | Change rendering setup rather than stacking adjectives |
| Text / exact dimensions wrong | State literal text, placement and typography; reduce competing visual instructions | External text/vector compositing; do not guarantee exact generator text |
| Character/product identity drift | Reuse original identity anchor; reduce competing images and shot complexity | Local identity-preserving editing/compositing where available |

After **2–3 targeted failures of the same kind**, stop blindly adding prohibitions: challenge the input geometry, reference roles, edit mode, model capability or required precision. Be explicit when generation cannot guarantee exact pixel or dimension fidelity.

## Comparison method

For A/B tests use same base, target model/interface and comparable settings, view at same resolution and crop. Vary one factor or tightly related group. Record task, model/version, input anchors, prompt change, visible outcome and failure rate where multiple outputs exist. Do not claim causality from a single run or invent unseen test results. Test image generation only on request.

## Delivery

For Nano Banana corrections deliver full, integrated **System Instruction** and **Prompt**, not a patch appended to an outdated prompt. For GPT Image corrections deliver one complete self-contained prompt. Keep output short unless user requests a full QA report.
