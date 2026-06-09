# Exam Sprint

Version: 1.5

Exam Sprint is a Codex skill for university final-exam rescue work. It turns lecture PDFs, notes, past papers, assignments, teacher-highlighted topics, and screenshots into zero-baseline-friendly question-type explanations, symbol decoders, visual cram cards, concrete practice tasks, wrong-answer repair, and sprint plans when planning is actually needed.

The default goal is not just to arrange study time. It is to help a student who may not understand the material yet quickly recognize what a problem is asking, what the symbols mean, what first step to write, and which small task to do next.

## What It Does

- Inventories course materials and identifies likely course modules.
- Detects exam-scoring style, such as calculation, conceptual explanation, memorization, practical skills, language work, or open-ended synthesis.
- Ranks topics by score gain under time pressure: exam likelihood, point value, learnability, prerequisite value, and material evidence.
- Defaults to Rescue Teaching Mode: symbol decoding, question-type recognition, plain-language templates, micro-examples, and first practice tasks.
- Uses compact tables, vertical step cards, readable mini flowcharts, and visual cram cards when they reduce cognitive load.
- Produces sprint plans only when the user gives remaining time or explicitly asks for scheduling.
- Supports answer checking, mistake analysis, and weak-point repair after the student attempts questions.
- Quickly probes PDFs so scanned or mixed files do not trap the workflow in long OCR attempts by default.

## Version 1.5 Highlights

- Shifted first-pass material outputs from broad rescue packs to concrete task boards.
- Added a task-card contract: source, why this task, first line or first decision, stop point, and self-check.
- Updated the probability golden case to name exact source tasks such as Chapter 7 page 27 exercise 7-1 question 5 and Chapter 6 page 42 comprehensive training question 4.
- Added a regression case for when users say the output is not useful because it stayed at topic level.

## Version 1.4 Highlights

- Added the first real golden regression case for probability materials-only rescue work.
- Added a canonical expected first pass that starts with material evidence, symbol decoding, question-type templates, and a concrete first practice task.
- Added a rubric to catch common failures such as overplanning, unexplained notation, weak source grounding, and missing practice.
- Added a user-facing probability rescue example for Chapter 6/7 materials.

## Version 1.3 Highlights

- Added a lightweight rescue artifact chain: material evidence -> rescue skeleton -> symbol and question-type cards -> practice task -> repair loop.
- Added reusable rescue output patterns for first-pass material maps, symbol decoders, question-type cards, micro-examples, and wrong-answer repair.
- Added subject playbooks so probability, conceptual courses, memorization courses, practical skills, language exams, and open-ended assessments get different rescue outputs.
- Added a self-review rubric focused on zero-baseline readability, first action, concrete practice, source grounding, and visual load.
- Added evaluation cases for future skill testing and regression checks.

## Version 1.2 Highlights

- Changed the default behavior from planning-first Sprint Mode to Rescue Teaching Mode.
- Added rules requiring symbols, abbreviations, formulas, and technical terms to be explained in plain language before use.
- Added visual-output guidance for compact tables, step cards, question-type maps, mini flowcharts, and visual cram cards.
- Added first-pass rescue tasks for cases where exam time is unknown.
- Updated the skill UI prompt to emphasize understanding key question types and knowing what to do next before building a schedule.

## Version 1.1 Highlights

- Added Sprint Mode and Deep Scan Mode.
- Added fast PDF handling rules for scanned and mixed PDFs.
- Added `scripts/pdf_probe.py` to quickly classify PDFs as text-readable, mixed, scan-first, or unreadable.
- Added provisional material maps when evidence is limited.
- Added optional probe caching for repeated testing on the same PDF.

See [CHANGELOG.md](CHANGELOG.md) for release notes.

## Installation

Clone this repository into your Codex skills directory:

```powershell
mkdir $env:USERPROFILE\.codex\skills -Force
git clone https://github.com/77lwd/exam-sprint.git $env:USERPROFILE\.codex\skills\exam-sprint
```

If the directory already exists, update it with:

```powershell
cd $env:USERPROFILE\.codex\skills\exam-sprint
git pull
```

Restart Codex or start a new conversation so skill metadata is reloaded.

## Project Structure

```text
exam-sprint/
  SKILL.md
  VERSION
  CHANGELOG.md
  agents/
    openai.yaml
  examples/
    probability-rescue-first-pass.md
  references/
    course-types.md
    evaluation-cases.md
    priority-rules.md
    pdf-dump-workflow.md
    rescue-output-patterns.md
    rescue-pipeline.md
    self-review-rubric.md
    subject-playbooks.md
  scripts/
    pdf_probe.py
  tests/
    golden/
      probability-materials-only/
        input.md
        expected.md
        rubric.md
```

## Notes

Exam Sprint uses the user's course materials as the primary source. The bundled references provide sprint methods and prioritization rules; they do not replace course-specific materials or promise exam scores.
