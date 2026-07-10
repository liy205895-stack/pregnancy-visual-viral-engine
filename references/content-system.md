# Content system

## Contents

1. Topic strategy
2. Semantic uniqueness
3. Visual specification
4. Nano Banana Pro prompt template
5. Required output schema
6. Safety and quality gates

## 1. Topic strategy

Model the viral structure of `@starbabyoffice` without copying its exact assets, wording, or concepts. Use immediate visual contrast, low language dependence, a couple-centered pose, an obvious support mechanism, and save/share utility.

Rank candidate ideas with this internal score (0–5 each):

- visual intimacy without explicitness
- correct/wrong contrast clarity
- pregnancy relevance
- novelty versus ledger
- one-frame comprehension
- animation potential
- share/save motivation

Reject candidates below 24/35. Prefer these families while keeping every exact geometry unique:

- bed and sofa closeness
- seated face-to-face partner support
- side-lying cuddle and repositioning
- standing embrace with wall/chair support
- kneeling or all-fours partner assistance
- getting into or out of bed
- partner-assisted stretching or relaxation
- pillow, wedge, headboard, chair, wall, or bed-edge support

Avoid generic exercise-only concepts unless a couple interaction is central.

## 2. Semantic uniqueness

Represent each topic with:

- canonical topic
- correct position
- wrong position
- setting
- woman orientation
- partner role
- main support prop
- educational focus

Consider two ideas duplicates when their correct and wrong body geometries are substantially the same even if the setting, title, or props differ. Use the ledger script for deterministic token similarity, then apply human semantic judgment.

## 3. Visual specification

Match the bundled references:

- vertical 9:16 poster, 1080x1920 target
- dark navy-black bedroom or domestic background
- large condensed uppercase white title
- top green-framed CORRECT panel with check icon
- bottom red-framed WRONG panel with cross icon
- same adult couple, wardrobe, room, lens, and camera angle in both panels
- realistic cinematic 3D medical visualization
- semi-transparent blue skin overlay revealing simplified skeletons
- fetus visible only through a tasteful anatomical cutaway of the pregnant abdomen
- green glow at supported alignment points
- restrained red/orange glow at discomfort or strain points
- 3–4 short callouts per panel, thin white leader lines, black rounded labels
- bottom disclaimer and three key reminders
- clean, legible, medically neutral, no gore

Improve on the references:

- use correct English spelling
- do not overcrowd with six labels per panel
- do not show deformed hands, duplicate limbs, impossible joints, intersecting bodies, or inconsistent fetal scale
- do not imply that one pose guarantees fetal safety
- keep text inside safe margins and away from TikTok UI zones

## 4. Nano Banana Pro prompt template

Write one self-contained English prompt with these ordered blocks:

1. `FORMAT AND PURPOSE`
2. `CONSISTENT CHARACTERS`
3. `TOP CORRECT PANEL`
4. `BOTTOM WRONG PANEL`
5. `MEDICAL OVERLAY`
6. `TYPOGRAPHY AND CALLOUTS`
7. `LIGHTING AND RENDER QUALITY`
8. `SAFETY AND NEGATIVE CONSTRAINTS`

Name exact poses and contact points. Specify what each hand, leg, torso, pillow, wall, or bed edge does. Do not rely on “make it safe.”

End every image prompt with a negative constraint equivalent to:

`No nudity, no explicit sexual act, no genital emphasis, no gore, no fetal distress, no extra limbs, no fused hands, no impossible anatomy, no misspelled text, no duplicated people, no changed wardrobe, no camera-angle mismatch, no watermark, no platform logo.`

Because image-model typography can fail, also supply an exact copy deck separately.

## 5. Required output schema

Return every accepted topic as:

### Topic ID and slug

- Chinese topic name
- English viral title, 5–10 words
- one-sentence hook
- novelty statement: why it is not a ledger duplicate
- setting
- correct pose: exact couple geometry
- wrong pose: exact couple geometry
- educational focus
- confidence flag: `general-comfort`, `needs-clinical-review`, or `clinically-sourced`

### Exact copy deck

- series title
- green header
- 3–4 green callouts
- red header
- 3–4 red callouts
- neutral disclaimer: `Educational visualization only. Comfort needs vary. Stop if painful and ask a qualified maternity-care professional when unsure.`
- three short reminders

### Nano Banana Pro image prompt

- one English prompt following Section 4

### Veo Omni video prompt

- one English prompt following `veo-omni-rules.md`

### Production notes

- recommended duration
- loop point
- on-screen UI safe-zone warning
- facts requiring clinical review

## 6. Safety and quality gates

Reject or revise output if any answer is yes:

- Does it depict minors or ambiguous age?
- Is either adult nude or engaged in an explicit sexual act?
- Does the camera emphasize breasts, buttocks, crotch, or fetishized body parts?
- Does it claim a pose is universally safe or that another directly harms the fetus without a cited clinical basis?
- Does it diagnose, prescribe, or replace professional care?
- Are the two panels inconsistent in characters, clothing, setting, or camera?
- Is the prompt too vague to reproduce the hand and body placement?
- Is it semantically duplicated in the ledger?

Use calm medical-education framing. Intimacy is conveyed through eye contact, gentle support, proximity, and coordinated positioning—not explicit action.
