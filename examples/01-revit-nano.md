# Revit to architectural photography — Nano Banana

<!-- Documentation example included in the v1.0 release. -->

Hypothetical example only; no image-generation result or measured image quality is claimed. The scene and attachment roles below are a synthetic user brief. Inspect real inputs before describing their visible details.

## User request

Use Nano Banana to turn my four-storey Revit hotel view into a clean daylight architectural photograph. Keep the six visible facade bays, roof, openings and camera. Specify cream honed limestone and dark bronze coated-aluminum frames.

## Expected modules

- [IMAGE_PROMPTING.md](../references/IMAGE_PROMPTING.md)
- [ARCHITECTURAL_FIDELITY.md](../references/ARCHITECTURAL_FIDELITY.md)
- [MATERIAL_REALISM.md](../references/MATERIAL_REALISM.md)
- [PHOTOGRAPHIC_REALISM.md](../references/PHOTOGRAPHIC_REALISM.md)

## Reference roles

Reference 1: hypothetical current Revit view, authoritative for visible geometry and camera. The written brief supplies the material map; no style image.

## Output format

Nano Banana: complete System Instruction + Prompt.

## Locked characteristics

Four storeys, six visible bays, opening and mullion layout, roof silhouette, site boundaries, camera and crop.

## Representative output

### System Instruction

```text
Reference 1 is the sole authority for the hotel's visible geometry and camera. Preserve four storeys, six visible facade bays, opening and mullion positions, roof silhouette, site boundaries and frame-edge cuts. Map solid facade bays to clean cream honed limestone with fine joints and restrained slab-to-slab ivory variation; map existing frames to dark bronze powder-coated aluminum. Keep the architecture newly constructed and maintained. Material and lighting changes may alter shading and reflections, never structural geometry. Add no people, cars, signs or new planting. Do not extrapolate unseen elevations.
```

### Prompt

```text
Convert the Revit hotel view in Reference 1 into one believable daylight architectural photograph using the material assignments above. Use soft directional daylight, coherent contact shadows, environment-consistent glazing reflections and controlled exposure retaining facade and sky detail. Show limestone variation at the existing camera distance without artificial dirt or damage. Keep the reference viewpoint, field of view, crop and all specified architectural counts. Deliver the finished view without annotations.
```
