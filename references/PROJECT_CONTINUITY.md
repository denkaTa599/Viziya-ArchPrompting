# Project continuity — consistent series without geometry contamination

Load if the request concerns multiple related views, recurring products/characters/places, repeat materials, an approved visual anchor or shot-to-shot consistency.

## Visual DNA ledger (short, not a giant prompt)

Define **global constants**: approved identities and their exact reference priority, material assignments and finishes, palette, architecture style, site/season, visual processing, and permitted atmospheric range. Define **per-shot variables**: camera/view, scene action, time-of-day when explicitly allowed, framing, newly visible geometry, local vegetation/people. Do not silently freeze a shot-specific detail into a global constant.

## Multi-view architectural precedence

- **Current native 3D view** determines its own geometry, camera, façade openings and crop.
- **Approved finished image** determines only designated materials, tonal style, planting identity or atmosphere, not old view layout.
- **Original face/product references** remain primary for identity; avoid using latest generated frame if it drifted.
- Each view must preserve its own horizon, perspective, level count and composition — never copy them from a different shot.

## Series strategy

1. Select an approved visual anchor and record a concise constant list.
2. Identify each new shot's *authoritative base* and permissible local differences.
3. Keep material names and finish descriptions consistent, but allow lighting-driven variation in appearance.
4. For changes to a project's design/material specification, update the constant list explicitly before future shots; do not retroactively assume earlier renders are geometry authorities.
5. For style drift, compare against the approved anchor, not the most recent generated image.
6. For long sessions, summarize only verified approved properties and carry them into a fresh self-contained prompt.

## Continuity QA

Check identity, clothing/product properties where required, number and arrangement of floors, palette, material zone mapping, glazing/frames, environmental season and lighting direction where specified. Do not treat all shots as requiring identical weather, shadows or exact grading if user approves editorial variation.

## Short prompt pattern

"For this view, Reference 1 controls all visible geometry and camera. Match only the approved material palette and photographic finish from Reference 2; retain the project's established glazing and cladding rules. Do not transfer Reference 2's viewpoint, façade layout, figures, vehicles or furniture."
