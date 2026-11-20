# New materials without artificial aging

Hypothetical example only; no image-generation result or measured image quality is claimed. The scene and attachment roles below are a synthetic user brief. Inspect real inputs before describing their visible details.

## User request

GPT Image: change only the limestone finish of a newly completed hotel to a less uniform natural appearance. Keep the existing geometry, panel sizes, camera and lighting.

## Expected modules

- [IMAGE_PROMPTING.md](../references/IMAGE_PROMPTING.md)
- [ARCHITECTURAL_FIDELITY.md](../references/ARCHITECTURAL_FIDELITY.md)
- [MATERIAL_REALISM.md](../references/MATERIAL_REALISM.md)

## Reference roles

Reference 1: hypothetical approved building render; geometry, camera and all non-target regions remain authoritative. No new material reference.

## Output format

GPT Image: one complete Prompt. No photographic module is needed for this material-only edit.

## Locked characteristics

Geometry, panel and joint dimensions, openings, frames, roof, lighting, exposure, crop and non-target materials.

## Representative output

### Prompt

```text
Edit only the cream honed-limestone facade bays in Reference 1. Give the new, carefully installed stone restrained non-periodic ivory variation between existing slabs, fine mineral variation and subtle changes in diffuse highlight behavior. At this medium architectural viewing distance, let slab tone and finish variation carry the realism; do not enlarge microscopic pores or scratches into visible patterns. Keep the building clean and newly completed, without added weathering, chips, cracks, corrosion or stains. Retain existing panel sizes, joints, wall depth, openings, frames, roof, camera and crop. Preserve lighting, global exposure, white balance and every non-target material; allow only reflectance changes physically caused by the revised stone finish. Return the locally edited view.
```
