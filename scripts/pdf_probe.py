#!/usr/bin/env python3
"""Fast PDF diagnostic probe for the exam-sprint skill.

This script intentionally does not OCR. It reports whether ordinary PDF text
extraction is likely enough for Sprint Mode, or whether the material should be
treated as scan-first and handled with a provisional map or Deep Scan Mode.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any


KEYWORDS = [
    "选择题",
    "多项选择题",
    "单项选择题",
    "填空题",
    "计算题",
    "证明题",
    "答案",
    "正确答案",
    "分布",
    "分布函数",
    "期望",
    "方差",
    "协方差",
    "正态",
    "估计",
    "假设检验",
    "置信区间",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sample_indexes(page_count: int) -> list[int]:
    if page_count <= 0:
        return []
    candidates = [0, 1, page_count // 2, page_count - 2, page_count - 1]
    return sorted({idx for idx in candidates if 0 <= idx < page_count})


def classify(sampled_pages: list[dict[str, Any]]) -> tuple[str, str]:
    if not sampled_pages:
        return "unreadable", "low"

    readable = sum(1 for page in sampled_pages if page["text_length"] >= 80)
    tiny = sum(1 for page in sampled_pages if page["text_length"] < 20)
    image_pages = sum(1 for page in sampled_pages if page["image_count"] > 0)
    total = len(sampled_pages)

    if readable >= max(1, total // 2 + 1):
        return "text-readable", "high"
    if tiny >= max(1, total // 2 + 1) and image_pages >= max(1, total // 2):
        return "scan-first", "high"
    if readable > 0 and tiny > 0:
        return "mixed", "medium"
    if tiny == total:
        return "unreadable", "medium"
    return "mixed", "low"


def recommended_action(status: str) -> tuple[str, str]:
    if status == "text-readable":
        return "Sprint Mode", "Continue normal text extraction and produce a prioritized sprint artifact."
    if status == "mixed":
        return "Sprint Mode", "Use readable pages for a first-pass map, then request targeted supplements for unreadable sections."
    if status == "scan-first":
        return "Sprint Mode", "Produce a provisional material map and request 1-3 high-value supplements; offer Deep Scan Mode if fuller extraction is needed."
    return "Sprint Mode", "Report limited evidence and request targeted supplements or a clearer source."


def cache_path(cache_dir: Path, sha256: str) -> Path:
    return cache_dir / f"{sha256}.json"


def read_cache(cache_dir: Path | None, sha256: str) -> dict[str, Any] | None:
    if cache_dir is None:
        return None
    path = cache_path(cache_dir, sha256)
    if not path.exists():
        return None
    try:
        with path.open("r", encoding="utf-8") as handle:
            cached = json.load(handle)
        cached["from_cache"] = True
        cached["cache_file"] = str(path)
        return cached
    except Exception:
        return None


def write_cache(cache_dir: Path | None, sha256: str | None, result: dict[str, Any]) -> None:
    if cache_dir is None or not sha256:
        return
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        path = cache_path(cache_dir, sha256)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(result, handle, ensure_ascii=False, indent=2)
    except Exception:
        return


def probe(path: Path, preview_chars: int, cache_dir: Path | None) -> dict[str, Any]:
    result: dict[str, Any] = {
        "file": str(path),
        "exists": path.exists(),
    }
    if not path.exists():
        result.update(
            {
                "error": "file_not_found",
                "status": "unreadable",
                "confidence": "high",
                "recommended_mode": "Sprint Mode",
                "recommended_action": "Ask the user to provide a valid file path or upload the material again.",
            }
        )
        return result

    stat = path.stat()
    result.update(
        {
            "file_name": path.name,
            "file_size": stat.st_size,
            "modified_time": stat.st_mtime,
        }
    )

    try:
        result["sha256"] = sha256_file(path)
    except OSError as exc:
        result["sha256_error"] = str(exc)

    cached = read_cache(cache_dir, result.get("sha256", ""))
    if cached is not None:
        return cached

    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - environment dependent
        result.update(
            {
                "error": "pypdf_import_failed",
                "error_detail": str(exc),
                "status": "unreadable",
                "confidence": "low",
                "recommended_mode": "Sprint Mode",
                "recommended_action": "Use a minimal material map from file metadata and request targeted supplements.",
            }
        )
        return result

    try:
        reader = PdfReader(str(path))
        page_count = len(reader.pages)
        result["page_count"] = page_count
        sampled_pages = []
        keyword_hits: dict[str, set[int]] = {keyword: set() for keyword in KEYWORDS}

        for idx in sample_indexes(page_count):
            page = reader.pages[idx]
            text = (page.extract_text() or "").replace("\x00", " ").strip()
            image_count = 0
            try:
                image_count = len(page.images)
            except Exception:
                image_count = 0

            for keyword in KEYWORDS:
                if keyword in text:
                    keyword_hits[keyword].add(idx + 1)

            sampled_pages.append(
                {
                    "page": idx + 1,
                    "text_length": len(text),
                    "image_count": image_count,
                    "preview": text[:preview_chars],
                }
            )

        status, confidence = classify(sampled_pages)
        mode, action = recommended_action(status)
        result.update(
            {
                "sampled_pages": sampled_pages,
                "status": status,
                "confidence": confidence,
                "keyword_hits": {
                    keyword: sorted(pages)
                    for keyword, pages in keyword_hits.items()
                    if pages
                },
                "recommended_mode": mode,
                "recommended_action": action,
            }
        )
        write_cache(cache_dir, result.get("sha256"), result)
        return result
    except Exception as exc:
        result.update(
            {
                "error": "pdf_probe_failed",
                "error_detail": str(exc),
                "status": "unreadable",
                "confidence": "low",
                "recommended_mode": "Sprint Mode",
                "recommended_action": "Report the read failure and request high-value supplements or a clearer export.",
            }
        )
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe PDF readability for exam-sprint.")
    parser.add_argument("pdf", help="Path to the PDF file.")
    parser.add_argument("--preview-chars", type=int, default=800)
    parser.add_argument(
        "--cache-dir",
        help="Optional directory for cached probe JSON files keyed by sha256.",
    )
    args = parser.parse_args()

    path = Path(os.path.expanduser(args.pdf))
    cache_dir = Path(os.path.expanduser(args.cache_dir)) if args.cache_dir else None
    result = probe(path, max(0, args.preview_chars), cache_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
