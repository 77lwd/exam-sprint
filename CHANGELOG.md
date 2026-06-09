# Changelog

## 1.3 - 2026-06-09

### Added

- Added a lightweight rescue pipeline inspired by production exam-prep workflows: material evidence -> rescue skeleton -> symbol and question-type cards -> practice task -> answer checking and repair.
- Added `references/rescue-pipeline.md` to define the first-pass artifact chain and rescue skeleton contract.
- Added `references/rescue-output-patterns.md` with reusable layouts for material-first packs, symbol decoders, question-type cards, micro-examples, and wrong-answer repair.
- Added `references/subject-playbooks.md` to choose different rescue artifacts for calculation, conceptual, memorization, practical, language, and open-ended courses.
- Added `references/self-review-rubric.md` for zero-baseline readability, first-action, practice-task, scope, and visual-load checks.
- Added `references/evaluation-cases.md` for future skill testing and regression checks.

### Changed

- Updated `SKILL.md` to load references selectively instead of relying on one large instruction body.
- Updated the default workflow to build a rescue skeleton before producing notes or plans.
- Updated `pdf_probe.py` recommendations to use Rescue Teaching Mode terminology.

## 1.2 - 2026-06-09

### Changed

- Shifted the default behavior from planning-first Sprint Mode to Rescue Teaching Mode for students who may not understand the material yet.
- Added symbol-decoding rules so formulas, acronyms, and notation are explained in plain language before being used as shortcuts.
- Added visual-output guidance for compact tables, vertical step cards, question-type maps, readable mini flowcharts, and visual cram cards.
- Updated the first-pass workflow to produce question-type templates, micro-examples, and concrete 30-90 minute rescue tasks when exam time is unknown.
- Updated the skill UI prompt to emphasize understanding key question types and knowing what to do next before building a schedule.

## 1.1 - 2026-06-09

### Added

- Added Sprint Mode and Deep Scan Mode for scan-heavy course materials.
- Added mode-switch guidance for cases where full extraction would materially improve quality but cost more time.
- Added fast PDF handling rules for text-readable, mixed, scan-first, and unreadable PDFs.
- Added `scripts/pdf_probe.py`, a lightweight JSON PDF diagnostic helper with optional SHA-256 cache support.

### Changed

- Scan-first PDFs now produce a provisional material map in Sprint Mode instead of triggering long default recovery attempts.
- Supplement requests now prioritize high-value evidence such as teacher emphasis, exam scope, past papers, answer keys, representative screenshots, and student weak topics.

### Notes

- `pdf_probe.py` does not perform OCR. Full OCR remains a future Deep Scan Mode enhancement.
