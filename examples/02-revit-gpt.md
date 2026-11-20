# Revit to architectural photography — GPT Image

Hypothetical example only; no image-generation result or measured image quality is claimed. The scene and attachment roles below are a synthetic user brief. Inspect real inputs before describing their visible details.

## User request

Use GPT Image for the same hypothetical four-storey, six-bay Revit hotel. Render clean honed limestone and dark bronze frames in natural daylight without redesigning the building.

## Expected modules

- [IMAGE_PROMPTING.md](../references/IMAGE_PROMPTING.md)
- [ARCHITECTURAL_FIDELITY.md](../references/ARCHITECTURAL_FIDELITY.md)
- [MATERIAL_REALISM.md](../references/MATERIAL_REALISM.md)
- [PHOTOGRAPHIC_REALISM.md](../references/PHOTOGRAPHIC_REALISM.md)

## Reference roles

Reference 1: hypothetical current Revit view controls geometry, perspective and crop. Material assignments come from the written user brief.

## Output format

GPT Image / ChatGPT Images: one complete Prompt.

## Locked characteristics

Storey/bay counts, opening layout, mullions, roof silhouette, site boundaries and source camera.

## Representative output

### Prompt

```text
Transform Reference 1, the supplied Revit hotel view, into one clean daylight architectural photograph. Use it as the sole authority for visible geometry and camera: retain four storeys, six visible facade bays, every opening and mullion, roof silhouette, site boundaries, perspective and crop. Apply cream honed limestone to solid facade bays, with fine joints and subtle non-repeating slab-to-slab variation, and dark bronze powder-coated aluminum to existing frames. Keep surfaces new and maintained. Use soft directional daylight, coherent contact shadows, plausible environment reflections and restrained tonal contrast. Allow the shading and reflections needed for photographic conversion while preserving the architecture. Add no people, cars, signs or new planting; do not invent unseen geometry. Return the finished view without annotations.
```
