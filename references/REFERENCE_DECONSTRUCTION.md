# Reference deconstruction — extract visual properties without copying geometry

Load for **style/material/lighting/composition transfer** from images. An image used solely as base geometry or identity does not trigger this module. Do not claim access to unseen references.

## Method

1. State which image is authoritative for **which property** (numbered input roles) and rank conflicts by property.
2. Describe only observable features: camera/composition, light direction and softness, atmosphere, material optical behavior, palette, texture scale, post-production/contrast. Distinguish **observed**, **inferred**, and **unknown**.
3. Define **transfer allowed** (e.g. warm soft illumination, matte limestone finish) and **not transferred** (a different building's silhouette, windows, landscaping layout, furniture, person identity, labels).
4. Describe how the transferred style interacts physically with the target: e.g. changing light can change target shadows, but does not change openings or façade rhythm.
5. Use the minimum relevant references; avoid mixing contradictory light treatments without choosing precedence.

## Compact 5-layer style analysis

- **Composition DNA:** viewpoint, framing, verticals, horizon/negative space, balance; only import when permitted.
- **Lighting DNA:** time/quality/direction, source size, shadow softness, exposure.
- **Material DNA:** finish, surface roughness, hue variation, reflectance, visible imperfections consistent with age.
- **Atmosphere DNA:** season, weather, haze, context, mood.
- **Processing DNA:** contrast, saturation, grain/clarity, tonal range, white balance.

A "Behance style" or a model/artist name is not enough by itself to specify transferable visual behavior; extract visible properties from available reference images. Avoid guessing the prompt, seed, model, camera EXIF, underlying material shader values, or exact location from a stylized image.

## Example role table

- Reference 1 — current Revit view; geometry and camera only.
- Reference 2 — approved finished view; material colors/finishes only.
- Reference 3 — photographic atmosphere; soft afternoon light and tonal treatment only.

Compose: "Match the approved warm daylight and restrained tonal contrast of Reference 3 on the unchanged geometry and framing of Reference 1; apply Reference 2's stone and glazing finishes only to the mapped surfaces." Do not silently import reference 3's building design.

## Check

Does each reference have a unique justified purpose? Could a secondary image corrupt geometry? Are style attributes visible or speculative? Is an approved existing style anchor more reliable than an arbitrary newer output?
