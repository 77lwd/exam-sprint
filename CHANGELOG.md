# Changelog

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
