---
name: exam-sprint
description: Emergency university exam preparation and final-exam sprint planning. Use when the user needs help turning lecture PDFs, slides, notes, past papers, assignments, teacher-highlighted topics, screenshots, or messy course materials into a practical cram plan, topic priority map, condensed review sheet, self-test questions, wrong-answer recovery loop, or last-minute exam strategy for any college course.
---

# Exam Sprint

## Version

Current version: 1.1

## Purpose

Help university students convert incomplete, messy course materials into a realistic final-exam sprint. Prefer practical triage over comprehensive study when time is short.

## Core Principles

- Do not block on incomplete information. Proceed with explicit assumptions and mark confidence.
- Optimize for score gain under time pressure: exam likelihood, point value, learnability, prerequisite value, and material evidence.
- Use the user's course materials as the primary source. Use this skill's references for method, not as a substitute for the teacher's materials.
- Ask at most three essential questions before producing a useful first pass.
- Separate "must rescue", "high yield", "if time remains", and "can skip for now".
- Default to fast sprint value. Do not spend several minutes recovering difficult files unless the user asks for fuller extraction or confirms a mode switch.

## Modes

Use **Sprint Mode** by default.

- Goal: produce a useful study direction quickly.
- Use when the user asks to review, cram, plan, prioritize, summarize likely topics, or make a first-pass map from course materials.
- For scan-first PDFs, keep probing short and produce a provisional artifact instead of attempting full OCR or repeated recovery paths.

Use **Deep Scan Mode** only when the user explicitly asks for complete extraction, comprehensive scanning, all questions, full OCR, a complete question bank, every-page organization, or says they are willing to wait.

- Goal: recover and structure as much of the material as possible.
- Briefly warn that it may take several minutes and that scan quality or missing OCR tools can limit accuracy.
- If the environment lacks reliable OCR/rendering tools, say so and offer targeted supplements as the faster path.

Prompt for a mode switch only when the mode materially changes quality or time cost:

- A scan-first file gives too little evidence for Sprint Mode.
- The user's requested artifact requires all pages or all questions.
- The user asks for more detail after a Sprint Mode first pass.
- Deep Scan Mode is possible but tool support or scan quality is uncertain.

Offer a concise two-option choice: continue Sprint Mode for a fast provisional artifact, or switch to Deep Scan Mode for fuller extraction with longer runtime.

## Default Workflow

1. Inventory the available materials.
2. For PDFs, run the fast PDF handling rules below before ad hoc extraction.
3. Infer the course structure from titles, sections, repeated terms, formulas, examples, diagrams, summaries, assignments, or past questions.
4. Classify the course by exam-scoring type. See `references/course-types.md`.
5. Rank topics by sprint priority. See `references/priority-rules.md`.
6. Ask only essential missing questions: exam time, exam format, and target outcome.
7. Choose a sprint strategy based on remaining time, mode, and confidence.
8. Produce the first usable study artifacts: roadmap, priority list, condensed notes, and self-test questions.
9. Iterate with answer checking, weak-point repair, and a final pre-exam sheet.

## Fast PDF Handling

When the user provides PDFs, prefer `scripts/pdf_probe.py` before manual extraction attempts. Use the probe's JSON output to decide whether the file is `text-readable`, `mixed`, `scan-first`, or `unreadable`.

If a PDF has already been probed, reuse cached probe results keyed by file hash when available. Cache diagnostic metadata only by default, not final study advice. Invalidate the cache when the file hash changes; if hashing is unavailable, use file size and modified time as a weak fallback.

In Sprint Mode:

- Keep scan-first probing to a short budget, roughly 30-90 seconds.
- Stop repeated fallback attempts after the probe and one high-value targeted check.
- Do not open local `file://` PDFs in a browser as a fallback.
- Do not do full OCR, full-page rendering, or multi-tool recovery unless the user confirms Deep Scan Mode.

For scan-first or mostly unreadable PDFs, produce a provisional material map instead of a full packet:

- Material status: page count, readable-text status, scan risk, and confidence.
- Visible evidence: only the pages, headings, keywords, or question types actually detected.
- Preliminary module map: 4-8 coarse modules, clearly marked provisional.
- Suspected high-yield topics: focus on sprint value and visible evidence.
- Missing evidence: directory, teacher emphasis, answer key, large-question pages, point structure, or past papers.
- Next best action: request only 1-3 high-value supplements.

Request supplements by score impact:

- Teacher emphasis, exam scope, marked topics, or review notice.
- Past papers, sample papers, answer keys, or point structure.
- Table of contents, module pages, chapter summary pages, or formula sheets.
- Two or three representative clear screenshots, chosen by material type.
- The student's own weak topics.

Adapt the request to the observed material type. For question sheets, prefer answer keys, marked topics, representative calculation pages, and confirmation of whether statistics chapters are included. For lecture dumps, prefer teacher emphasis, past papers, and module or summary pages.

## PDF Dump Workflow

When the user uploads or points to multiple lecture PDFs/slides, use `references/pdf-dump-workflow.md`.

First produce a material map before writing a full review packet:

- File or chapter inventory
- Detected course modules
- Probable course type mixture
- Suspected high-yield topics
- Missing evidence and confidence level
- Suggested next action

## Minimal Questions

Ask no more than these unless the task truly cannot continue:

1. When is the exam, or how many study hours remain?
2. Is it closed-book, open-book, machine exam, oral exam, paper/project, or unknown?
3. Is the goal passing, stable score, high score, or emergency rescue?

If the user does not answer, proceed with assumptions and state them briefly.

## Output Artifacts

Choose artifacts that match the user's urgency:

- Material inventory
- Course structure map
- Topic priority table
- 24-hour, 3-day, or 7-day sprint plan
- One-page cram sheet
- Formula, definition, keyword, or process checklist
- Practice questions without immediate answers when drilling
- Answer key and mistake analysis after the user attempts questions
- Final 20-minute pre-exam sheet

## Confidence Labels

Use simple confidence labels:

- High: teacher highlights, past papers, assignments, and lecture emphasis agree.
- Medium: lecture structure and repeated material suggest importance, but past papers or teacher highlights are missing.
- Low: little course-specific evidence is available; the plan relies mostly on general course patterns.

## Boundaries

- Do not promise score outcomes.
- Do not fabricate teacher-specific exam predictions.
- Do not generate huge exhaustive notes when a prioritized plan would help more.
- Do not rely on web search unless the user asks or local materials are insufficient and current external facts are genuinely needed.
