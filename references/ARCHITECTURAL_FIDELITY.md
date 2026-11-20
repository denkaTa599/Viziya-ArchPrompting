# Architectural fidelity — geometry-preservation contract

Use only when routed by `../SKILL.md`. Purpose: retain the architect's design rather than generate an appealing but incorrect substitute.

## Priority evidence

- **Authoritative current view / model:** exact visible geometry, openings, count of storeys, façade rhythm, roof and parapet outlines, structural projections, major landscaping boundaries, camera, crop and horizon.
- **Approved material reference:** assigned colors, finishes and reflections only; never transfer its unrelated façades, furniture, plants or camera.
- **Project brief:** explicit changes and facts follow the precedence in `../SKILL.md`. An authorized design change updates only the named invariant; all other approved geometry stays locked. Resolve consequential conflicts before inventing a replacement design.
- **Model guesses:** never override the above. Missing elevation, hidden side or exact measurement from an image are unknown, not permission to invent.

## Minimal internal preservation contract

Before drafting, sort relevant properties into:
- **LOCKED**: must not change (visible geometry, specified modules, visible number of storeys, existing glazing/rails, approved camera, site boundaries).
- **EDITABLE**: user-authorized objects/regions and physical secondary effects (new materials → reflectance changes; new vegetation → contact shadows).
- **OBSERVED**: directly supported by supplied images, but not necessarily exact dimensions.
- **INFERRED / UNKNOWN**: interpretation, occluded parts and measurements not reliably visible; avoid unsupported assertions.

Do not show an exhaustive contract unless it helps diagnose a difficult architectural case. For a complex building, identify a small set of image anchors: extremities and edge cuts, distinctive corners, slab lines, horizon or sky share, known cores, façade bay counts, roof silhouette, balconies, mullions, ground/sea orientation. Preserve important count constraints exactly.

## Camera and geometry rules

- Existing view edit: same camera position/orientation, perspective, field of view, crop; do not simultaneously request an incompatible new angle or lens.
- New view: explicitly authorize camera movement and preferably use a new native view. Reconstructing unseen façades from one screenshot is unreliable.
- Plan/section: maintain orientation, relationships, line hierarchy, annotation and technical data; generate atmosphere only behind reliable geometry overlays.
- Do not turn a curved/modular footprint into a straight wing or flatten stepping because a cleaner photo seems easier.
- Added people/trees/cars must not hide required geometry, exits or glazing; keep correct scale and plausible ground contact.

## Materials without geometry drift

Describe each surface by **specific element → material → hue → finish → scale**. A material edit may alter physically consistent shading/reflections, not wall depth, joint spacing unrelated to the design, window size or structural geometry. Imperfections may affect *surface appearance* but must not create fake chips, cracks or form changes in new architecture. Use `MATERIAL_REALISM.md` only if the router triggers it.

## What to do on fidelity failure

1. Identify the first broken invariant (e.g. right-hand stair bay deleted, façade fin count changed, camera cropped).
2. Return to authoritative original base, not a generated frame that already contains the deformation.
3. Isolate the edit; reduce competing style references; crop or mask the relevant region if the tool supports it.
4. Ask for a fresh modeling view for a truly different viewpoint or invisible geometry.
5. Never promise a textual constraint can guarantee geometrical exactness or substitute for CAD verification.

## Concise sample directive (adapt, do not paste blindly)

"Use Reference 1 as the sole authority for the visible building geometry and camera. Preserve the exact number of storeys, existing window and mullion layout, balcony edges, façade projections, roof line and frame-edge cuts. Change only the named façade material and its physically necessary reflections/shadows. Do not extrapolate hidden geometry."
