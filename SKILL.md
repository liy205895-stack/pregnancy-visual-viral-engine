---
name: pregnancy-visual-viral-engine
description: Generate non-repeating pregnancy safety viral topics centered on a clothed adult couple, especially correct-versus-wrong intimate support positions, then produce English Nano Banana Pro image prompts matching the bundled dark medical infographic references and Veo Omni image-to-video prompts. Use when Codex needs TikTok or YouTube Shorts topic ideation, pregnancy couple visual concepts, prompt packages, content-batch planning, or duplicate-safe topic management for this account.
---

# Pregnancy Visual Viral Engine

Generate a production-ready package, not loose ideas. Default to English on-screen copy and prompts, with concise Chinese explanations unless the user requests another language.

## Required workflow

1. Read `references/content-system.md` for topic rules, visual grammar, safety boundaries, and output schema.
2. Read `references/veo-omni-rules.md` before writing any video prompt.
3. Treat `assets/style-reference-01.png` and `assets/style-reference-02.png` as the visual references. Inspect them when image viewing is available.
4. Check uniqueness before presenting a topic:

   ```bash
   python scripts/topic_ledger.py check --topic "<canonical topic>" --correct "<correct position>" --wrong "<wrong position>"
   ```

5. If it is a duplicate or near-duplicate, discard it and generate another. Do not rename an old concept to evade the check.
6. Reserve every topic included in the final answer before returning it:

   ```bash
   python scripts/topic_ledger.py reserve --topic "<canonical topic>" --correct "<correct position>" --wrong "<wrong position>" --slug "<slug>" --owner "<employee or unknown>"
   ```

7. Return the topic package using the exact schema in `references/content-system.md`.

## Non-repetition contract

- Define uniqueness semantically, not only by title. Changing “supported seated embrace” to “safe seated cuddle” is still a duplicate if the couple geometry, support mechanism, and risk contrast are the same.
- Vary at least three of these dimensions from prior entries: setting, body orientation, support prop, partner role, correct mechanism, wrong mechanism, camera angle, educational focus.
- Never reuse the same correct/wrong pair.
- Do not reset or delete the ledger during normal use.
- For team use, pull the latest repository state before generation and commit `data/used-topics.json` immediately afterward. Resolve ledger conflicts by retaining all entries.

## Generation defaults

- Prioritize a visibly pregnant adult woman and her adult male partner as requested.
- Favor affectionate, intimate-looking but non-explicit poses: supported embrace, side-lying cuddle, seated face-to-face support, partner-assisted repositioning, bed-edge support, kneeling support, pillow-assisted closeness.
- Keep both adults fully clothed in fitted, opaque athletic or sleepwear. No nudity, intercourse, genital focus, fetish framing, or pornographic camera angles.
- Frame content as general educational visualization, not individualized medical advice.
- Use “more supported / less supported” language when medical certainty is weak. Do not invent fetal distress, compression, circulation, or injury claims.
- Generate image prompts for a clean 9:16 two-panel infographic. Ask the image model for exact short English labels, but also return a separate copy deck because generated text may require manual correction.
- Generate Veo Omni prompts as controlled image-to-video animation prompts. Preserve layout, anatomy, text, and panel boundaries.

## Batch requests

For a requested batch, generate and validate candidates one at a time. Reserve all accepted topics. If reservation fails because another worker claimed one, replace it before delivering the batch.

## Failure handling

- If the ledger is unavailable, do not claim global uniqueness. State that uniqueness is only checked within the current conversation and provide commands to initialize or repair the ledger.
- If the user requests medically unsafe or explicit imagery, preserve the educational goal while converting it to clothed, non-explicit couple positioning.
- If current Veo product behavior conflicts with the bundled rules, follow the user's stated interface requirements and note the applied variant.
