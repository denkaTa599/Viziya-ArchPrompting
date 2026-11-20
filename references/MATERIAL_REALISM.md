# Material realism and physically justified imperfections

Read only if the router triggers material-specific work. Aim for *photographically credible clean materials* before considering wear. No universal rule demands dirt, scratches, five defects, noise, grunge, or aging.

## Material reasoning ladder

1. **Identity & finish**: What exactly is it (honed limestone, powder-coated aluminum, low-iron glass, exposed concrete, unfinished oak)? Finish is as important as material name.
2. **Intrinsic variation**: Mineral bands, natural grain, pores, inclusions, board/slab-to-slab changes inherent to the material.
3. **Manufacturing/installation variation**: Surface treatment, subtle finish differences, joints, panel scale, grain orientation, fabrication signatures consistent with quality of installation.
4. **Environment & exposure**: Rain paths, coastal spray, UV, moisture, hand contact, abrasion and sheltered versus exposed regions — only if time/exposure warrants them.
5. **Age, maintenance & scene intent**: New, lived-in/maintained, aged/weathered. Never infer old from "photorealistic".
6. **Visibility at camera distance**: At wide view: larger tonal/panel variation, coherent reflections. At medium: seams, grain, roughness changes. At detail: pores, fine brush marks and fine imperfections. No macro-sized micro-scratches at aerial distance.

## Three distinct levels (select from brief, not automatically user-facing)

- **Level 1 — New / carefully maintained (default for unspecified contemporary architecture):** realistic intrinsic and fabrication variance; generally clean; avoid chipped corners, corrosion and stains.
- **Level 2 — Occupied / mildly weathered:** small exposure-led water traces, contact marks, mild dust where plausible; not uniform aging across every panel.
- **Level 3 — Old / intentionally weathered:** patina, erosions, deposits, finish loss and other material-specific effects in physically plausible locations, consistent with building age and climate.

The levels control surface *appearance*, not a demand to invent geometry or change designed cladding module sizes.

## Material behavior mini-library

| Material | Visually credible variation | Common failure to avoid |
|---|---|---|
| Honed limestone/natural stone | slight tile-to-tile ivory variation, fine pores, restrained veins, matte diffuse response, realistic joints | identical tiling, high-gloss plastic stone, exaggerated cracks/dirt |
| Powder-coated aluminum | uniform base color with angle-sensitive highlights; finish-consistent microscopic texture | arbitrary rust, huge scratches, changing frame geometry |
| Brushed metal | directional anisotropic reflection with correct grain direction and restrained microvariation | every surface reflecting identically regardless of angle |
| Architectural glass | environment-correct reflections, angle-dependent reflectance, transparency linked to lighting/background, coherent mullion continuity | opaque mirrors everywhere, impossible reflections, random dirt |
| Concrete | natural pore distribution, controlled casting/aggregate variance, plausible formwork evidence if appropriate | strong procedural cloud noise, fake damage |
| Timber | distinct non-repeating board grain, longitudinal fibers, moderate hue variation, plausible finish absorption | duplicated identical boards, cross-grain where impossible |
| Painted plaster | coherent fine texture, diffuse response, local imperfections only as appropriate | splotchy dirty surfaces on a new building |
| Water | surface ripples scaled to pool/sea, physically plausible refraction, scene-coherent reflections, depth/color gradient | flat neon uniform color or nonsensical ripples |

## Spatial placement of imperfections

- Rain streaks occur below relevant edges, drainage points, parapets, joints or runoff paths — not randomly on all surfaces.
- Contact marks cluster near handles and frequently touched elements, not high inaccessible glazing by default.
- UV/exposure affects sun-facing surfaces and exposed timber; water deposits depend on orientation, climate and drainage.
- Coastal atmosphere alone does not justify heavy corrosion on new coated aluminum or visible salt crust on every pane.
- Roughness variation is mostly visible as *changes in highlight behavior*, not necessarily colored stains.
- Irregularity should be restrained and **non-periodic**. Avoid procedural repetition or artificial noise that looks like a filter.

## Prompt generation pattern

Use one compact clause per principal material: **surface/zone + exact material/finish + macro-scale organization + subtle intrinsic variation + view-scale-appropriate optical response + allowed age/exposure**. For clean new work, say so affirmatively. Add a short exclusion only if prior failure makes it necessary.

Example: "Cream-white honed limestone on the solid façade bays, with fine joints, subtle slab-to-slab ivory variation, natural micro-porosity and softly non-uniform diffuse reflection; new, carefully installed and clean, without artificial distressing."

## PBR translation rule

Words such as roughness, normal/bump, anisotropy or specular response can describe observable effects, but text prompts do **not** edit actual shader nodes or output exact PBR maps. If the workflow explicitly asks for editable texture maps, a dedicated material workflow is required. Do not claim measured IOR, roughness values, map scale or physically verified BRDF from a photo without supporting evidence.

## Interaction with geometry and reference roles

Respect geometry/mullions/element location fixed by architectural base. Material reference determines only permitted material characteristics. A weathered photo does not mean weather the new building unless approved. If a material changes reflections/tonality, permit corresponding localized visual changes while preserving geometry.
