# Veo Omni image-to-video rules

## Contents

1. Operating assumption
2. Mandatory prompt order
3. Motion limits
4. Negative constraints
5. Prompt template

## 1. Operating assumption

Treat the Nano Banana Pro poster as the input image and request a single controlled image-to-video shot. The image defines composition, characters, anatomy, wardrobe, labels, colors, lighting, and panel layout. The video prompt defines motion only where possible; do not redescribe or reinterpret the scene unnecessarily.

Default output: vertical 9:16, 8 seconds, one continuous locked shot, silent, seamless or near-seamless loop.

## 2. Mandatory prompt order

Write prompts in this order:

1. input-image preservation instruction
2. camera behavior
3. top-panel motion timeline
4. bottom-panel motion timeline
5. medical-overlay animation
6. ending and loop behavior
7. negative constraints

Use timestamps or short phases. Ask for one primary motion per phase. Keep physical movement small to protect anatomy and text.

## 3. Motion limits

- Lock camera and composition. No zoom, pan, tilt, orbit, reframing, cuts, transitions, or panel swaps.
- Preserve both panels on screen for the entire clip.
- Preserve every word exactly; animate only a subtle glow or opacity pulse around text, never individual letters.
- Keep faces, identity, hands, limb count, clothing, fetus, skeleton, and body contact points consistent.
- Use micro-motion: breathing, blink, tiny head movement, gentle hand settling, restrained green support pulse, restrained red strain pulse, leader-line shimmer.
- Do not animate the fetus independently beyond an extremely subtle ambient presence; never depict distress.
- Do not turn an incorrect pose into a correct pose. The comparison stays spatially stable.
- Avoid large partner or limb movement; use motion intensity of roughly 5–10%.
- Keep physics natural and contact stable. No sliding, penetration, melting, morphing, or rubber limbs.
- End on a frame visually close to the input for looping.
- Default to no generated speech, captions, sound effects, or music. Audio can be added in editing.

## 4. Negative constraints

Always include:

`No camera movement, no cuts, no transition, no crop change, no text mutation, no new text, no misspelling, no logo, no watermark, no anatomy change, no face change, no extra fingers, no extra limbs, no body intersection, no clothing change, no sexual motion, no nudity, no gore, no fetal distress, no flicker, no warping, no morphing, no object appearing or disappearing.`

If the Veo interface offers a separate negative-prompt field, put the constraints there; otherwise append them to the main prompt.

## 5. Prompt template

```text
Use the supplied vertical two-panel pregnancy safety infographic as the exact first-frame and composition reference. Preserve the same two adult characters, faces, clothing, anatomy, fetus visualization, typography, labels, colors, panel borders, background, and all body contact points.

CAMERA: Locked-off 9:16 shot for [8] seconds. Both panels remain fully visible. No camera motion or editing.

0.0–2.0s: [one subtle establishing motion].
2.0–5.0s: In the green top panel, [small breathing/hand-settling motion]; [green alignment/support glow] gently travels once along [specific area].
2.0–5.0s: In the red bottom panel, keep the pose fixed; [red/orange strain glow] pulses gently at [specific area], without implying injury.
5.0–7.0s: [callout dots/leader lines] brighten sequentially while all text remains perfectly static and readable.
7.0–8.0s: Motion settles back toward the original frame for a seamless loop.

[negative constraints]
```

If starting from text rather than an image, include the full image specification from `content-system.md`, but still use one locked shot and the same motion limits.
