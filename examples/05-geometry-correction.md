# Correcting geometry drift — Nano Banana

Hypothetical example only; no image-generation result or measured image quality is claimed. The scene and attachment roles below are a synthetic user brief. Inspect real inputs before describing their visible details.

## User request

Nano Banana: my generated hotel image changed the opening count in the right-hand facade. Correct it from the original Revit view and retain the already approved cream stone and daylight treatment.

## Expected modules

- [IMAGE_PROMPTING.md](../references/IMAGE_PROMPTING.md)
- [ARCHITECTURAL_FIDELITY.md](../references/ARCHITECTURAL_FIDELITY.md)
- [VISUAL_QA.md](../references/VISUAL_QA.md)

## Reference roles

Reference 1: hypothetical original Revit view, geometry/camera authority. Reference 2: hypothetical failed result, only a reported defect locator. Cream stone and daylight are already approved written facts, not new appearance-analysis requests.

## Output format

Nano Banana: both full System Instruction and Prompt, including on correction. A real diagnosis must inspect available images; this written example does not verify a visible defect.

## Locked characteristics

All approved geometry outside the faulty opening arrangement, source camera/crop, cream stone and approved daylight treatment.

## Representative output

### System Instruction

```text
Reference 1 is the sole authority for visible building geometry, opening counts and camera. Reference 2 is a failed result and must not become the geometry standard. Retain the approved cream-stone material assignment and daylight treatment while correcting only the reported right-hand facade opening drift. Preserve other approved architectural features and the original roof, storeys, frame positions, perspective and crop. Allow only the local shading and reflections necessary for the corrected geometry. Do not redesign adjacent regions or add objects.
```

### Prompt

```text
Restore the right-hand facade opening arrangement exactly as visibly specified by the original model view in Reference 1. Use Reference 2 only to identify the user-reported failure, not to infer a new design. Keep the approved cream stone and daylight appearance, and preserve all unaffected architectural features and camera anchors. Return one corrected view. If the source does not make the openings readable, request a clearer native view instead of inventing their arrangement; after repeated drift, use supported local masking/compositing or a geometry-correct source rather than expanding the style instructions.
```
