# Changelog

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
