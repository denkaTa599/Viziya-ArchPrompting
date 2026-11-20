# A consistent architectural series

Hypothetical example only; no image-generation result or measured image quality is claimed. The scene and attachment roles below are a synthetic user brief. Inspect real inputs before describing their visible details.

## User request

Nano Banana: create a consistent set of photorealistic hotel views from three native Revit views. Use an approved appearance image for cream limestone, bronze frames and restrained daylight photography, without copying its camera or facade layout.

## Expected modules

- [IMAGE_PROMPTING.md](../references/IMAGE_PROMPTING.md)
- [ARCHITECTURAL_FIDELITY.md](../references/ARCHITECTURAL_FIDELITY.md)
- [MATERIAL_REALISM.md](../references/MATERIAL_REALISM.md)
- [PHOTOGRAPHIC_REALISM.md](../references/PHOTOGRAPHIC_REALISM.md)
- [REFERENCE_DECONSTRUCTION.md](../references/REFERENCE_DECONSTRUCTION.md)
- [PROJECT_CONTINUITY.md](../references/PROJECT_CONTINUITY.md)

## Reference roles

For each shot attach Reference 1: that shot's current native view. Reference 2: hypothetical approved appearance anchor, assigned material palette/finish and photographic tone only. Inspect both in real use. Reuse the same approved anchor across shots.

## Output format

Nano Banana: a complete pair for each shot. The pair below is reusable for each independently attached current view, without relying on another chat.

## Locked characteristics

Each current native view's geometry, opening/storey counts, roof, camera and crop. Global constants: cream honed limestone, bronze coated frames, clean/new condition and restrained daylight tone.

## Representative output

### System Instruction

```text
For every shot, its current native view in Reference 1 is the sole authority for visible geometry and camera. Preserve that view's opening and storey counts, facade layout, roof outline, perspective and crop. Reference 2 controls only the approved cream honed-limestone finish, bronze powder-coated frame finish and restrained daylight photographic treatment. Keep these material assignments and the clean newly completed condition consistent across the series, with subtle intrinsic variation at each shot's viewing distance. Do not import Reference 2's facade layout, viewpoint, furnishings, people or planting. Keep physically coherent shadows and reflections appropriate to each current view.
```

### Prompt

```text
Produce the current hotel's architectural photograph from Reference 1. Apply only the material appearance and photographic tone assigned to the approved anchor in Reference 2. Preserve the current view's geometry, camera, field of view and crop, including newly visible geometry specified by that native view. Match cream limestone and bronze frame identity across the series while allowing view-dependent highlights and reflections. Use coherent natural daylight and restrained tonal contrast. Add no new objects. Return this single finished view, then compare its material/tonal consistency to the approved anchor before proceeding to the next native view.
```

For the next shot, replace only Reference 1 with the next native view. Keep the approved appearance anchor; do not make the latest generation the default anchor. If the design changes, update the written constants explicitly before continuing.
