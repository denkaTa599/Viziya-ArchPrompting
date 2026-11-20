# Sources, attribution and licensing notes

The following public projects informed the **conceptual approach** to material realism, structured prompt writing, architectural preservation, iterative critique and reference analysis. This project uses **newly written text**; it does not claim its source projects endorse or maintain this work.

- `dakhlallah/arch-render`: https://github.com/dakhlallah/arch-render — architectural views, camera/fidelity and material references.
- `olegspiridonovdev-spec/photoreal-image-skill`: https://github.com/olegspiridonovdev-spec/photoreal-image-skill — structured prompting and image critique.
- `Sugamdeol/UltraReal-Prompt-Architect`: https://github.com/Sugamdeol/UltraReal-Prompt-Architect — photographic/material reasoning.
- `ricardochristovao/photorealistic-skill`: https://github.com/ricardochristovao/photorealistic-skill — realism audits.
- `jiemianduan/image-to-prompt`: https://github.com/jiemianduan/image-to-prompt — extracting observable appearance from image references.
- `Bartindigital/blender-hyperrealism-skill`: https://github.com/Bartindigital/blender-hyperrealism-skill — physically plausible surface imperfection logic.
- `boli-bang/sketchup-render-workflow`: https://github.com/boli-bang/sketchup-render-workflow — multi-view project workflows.
- `Emily2040/nano-banana-image-skill`: https://github.com/Emily2040/nano-banana-image-skill — image model workflows and consistency.
- `youyouhdhd/cad-ai-renderer`: https://github.com/youyouhdhd/cad-ai-renderer — structural reference workflows (not directly reproduced here).

Official model docs (consult when version-specific):
- https://developers.openai.com/api/docs/guides/image-generation
- https://developers.openai.com/api/docs/guides/image-prompting
- https://ai.google.dev/gemini-api/docs/image-generation

**Published-project policy (v1.0):** compatibility and performance claims must identify their actual evidence. The package's static checks and text-agent routing traces are not image-quality benchmarks. Check the current license and attribution requirements before incorporating any third-party text, code or assets; conceptual links are not permission to copy them. No third-party code or images are bundled.

**Licensing decision pending:** this public repository does **not include a LICENSE**. The owner has not selected reuse terms; no MIT or other license has been added automatically. Do not imply that source-project licenses apply to this independent work. Contributors should avoid adding third-party content until its permissions and the project's licensing decision are resolved.

Tooling documentation consulted for the v1.0 workflow (not bundled):
- https://learn.chatgpt.com/docs/build-skills
- https://github.com/actions/checkout/releases/tag/v7.0.1
- https://github.com/actions/setup-python/releases/tag/v7.1.0

The validation and opt-in Codex CLI harness use Python's standard library. Ordinary CI requires no model credentials or generation services. Hypothetical examples contain no third-party images and claim no successful image-generation results.
