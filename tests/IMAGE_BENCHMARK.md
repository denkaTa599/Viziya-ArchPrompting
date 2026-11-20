# Comparative image-generation benchmark — not executed

This is a prepared protocol, not evidence of image quality. Do not run generations without a separate explicit request, model access and an agreed spending limit. Text-only Codex routing tests are a different experiment.

## Scope and controls

Compare Viziya ArchPrompting v1.0 against the baseline prompting approach below on both Nano Banana and GPT Image. Use the same owned or appropriately licensed input images, written briefs, attachment order, approved geometry/material facts, output size and comparable interface settings. Record each exact model/version/interface and date; do not assume shared seeds or unsupported controls. Keep the selected family fixed within each comparison.

**Baseline prompting approach:** write a direct prompt from the shared brief and supplied references without loading Viziya's router or reference modules. State the requested transformation, numbered reference roles, locked geometry/camera, materials/lighting, permitted edits and deliverable using only the supplied facts. Use the same prompt author and preparation budget for both approaches. Document and freeze the baseline method and each arm's complete prompts before any generation; do not tune either arm after seeing outputs.

Use six tasks: Revit daylight conversion, facade material-only replacement, clean new-building imperfections, old-building weathering, reference lighting transfer, and geometry-drift correction. For correction, use the same original base and failed result in both approaches. Include one additional multi-view series if an approved set of native views is available; do not infer unseen geometry.

Prepare prompts independently using v1.0's actual instructions for the skill arm and the documented baseline method for the baseline arm. Save complete Nano Banana System Instruction + Prompt pairs or one complete GPT Image Prompt for both arms. Keep prompts and inputs unchanged across repeated samples within an arm.

## Proposed initial size

Six tasks × two prompting approaches × two model families × two outputs = **48 images**. This is a small exploratory comparison, not a reliable general failure-rate estimate. Price and availability must be checked when execution is authorized. If that exceeds the agreed budget, reduce the task set explicitly rather than quietly dropping failed outputs. Multi-view work is a separately budgeted extension.

## Evaluation order

1. Critical architectural invariants: storeys, opening/bay counts, roof silhouette, geometry, approved camera/crop and exact required text. Any critical violation is recorded as a failure before aesthetic scoring.
2. Edit/reference scope: unchanged regions, approved material mapping, no contamination by unrelated reference geometry or objects.
3. Physical plausibility: coherent lighting/shadows/reflections; texture scale and non-repetition; imperfections justified by material, age, exposure and viewing distance.
4. Photographic finish and, for the extension, series consistency against an approved anchor.

Randomize prompting-approach labels for review where practical. Use the same viewing size/crop and a written rubric. Record all outputs and all failures, including refusals or inaccessible tools; do not cherry-pick. If two reviewers are available, record disagreements instead of hiding them in one average.

## Evidence record

For every attempt record: task ID, prompting approach, v1.0 skill commit or frozen baseline-method revision, model/version/interface, timestamp, input hashes and roles, full prompt blocks, supported settings, generated output location, generation time/cost if available, critical pass/fail, category scores, reviewer notes and comparison limits. Use only project-owned/licensed material and avoid publishing private images or credentials.

After 2–3 repeated failures in a category, test a documented change of strategy (clearer native base, supported mask/compositing or manual geometry correction) as a **separate experiment**, rather than rewriting prompts mid-comparison.

## Permitted conclusion

Report observations only for the tested scenes, prompting approaches, model versions and settings. A routing improvement, shorter context or a more attractive single output is not proof of higher image quality. Keep static checks, deterministic scoring, live text-agent behavior and generated-image evidence separate in the final report.
