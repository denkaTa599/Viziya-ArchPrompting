# Reference lighting and photographic style

Hypothetical example only; no image-generation result or measured image quality is claimed. The scene and attachment roles below are a synthetic user brief. Inspect real inputs before describing their visible details.

## User request

GPT Image: apply the soft overcast light and neutral tonal treatment of reference 2 to the building in reference 1. Preserve all materials and architecture.

## Expected modules

- [IMAGE_PROMPTING.md](../references/IMAGE_PROMPTING.md)
- [ARCHITECTURAL_FIDELITY.md](../references/ARCHITECTURAL_FIDELITY.md)
- [PHOTOGRAPHIC_REALISM.md](../references/PHOTOGRAPHIC_REALISM.md)
- [REFERENCE_DECONSTRUCTION.md](../references/REFERENCE_DECONSTRUCTION.md)

## Reference roles

Reference 1: hypothetical approved target building, geometry/camera/material assignments. Reference 2: hypothetical photo whose user-specified overcast light and neutral tone may transfer; not its building, objects or framing.

## Output format

GPT Image: one complete Prompt.

## Locked characteristics

Target silhouette, storeys, openings, facade layout, material identity, camera and crop. Global light/shadows/reflections may change.

## Representative output

### Prompt

```text
Relight the building in Reference 1 using only the soft overcast illumination and neutral photographic tonal treatment assigned to Reference 2. Reference 1 remains authoritative for its visible architectural geometry, material identities, camera, framing and crop. Preserve storeys, openings, mullions, facade rhythm and roof silhouette. Transfer broad diffuse sky illumination, soft coherent shadows, balanced facade exposure and restrained contrast; permit corresponding scene-wide reflection, shadow and white-balance changes. Do not transfer Reference 2's architecture, composition, vegetation, furniture, people or signs. Keep the target's existing objects and material assignments. Deliver one photographic view with the original target geometry and viewpoint.
```
