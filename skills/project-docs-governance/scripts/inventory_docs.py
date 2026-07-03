#!/usr/bin/env python3
"""Inventory documentation governance health for a repository.

This script is read-only. It helps agents decide whether to bootstrap, migrate,
audit, or repair a docs system.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


RECOMMENDED = [
    "AGENTS.md",
    "docs/README.md",
    "docs/contributing/documentation.md",
    "docs/contributing/cross-cutting-concerns.md",
    "docs/product/vision.md",
    "docs/planning/roadmap.md",
    "docs/planning/implementation-status.md",
    "docs/architecture",
    "docs/reference",
    "docs/adr",
]

RULE_ID_RE = re.compile(r"Rule ID:\s*`([^`]+)`")
ADR_RE = re.compile(r"^\d{4}-.+\.md$")
STATUS_RE = re.compile(r"^\s*(?:>\s*)?(?:Doc\s+)?Status:\s*([A-Za-z][A-Za-z -]*)\s*$", re.IGNORECASE | re.MULTILINE)
PLAN_STATUS_RE = re.compile(r"\b(Planned|In progress|Shipped|Partial|Deferred|Dropped|Superseded)\b")


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def count_markdown(root: Path, path: str) -> int:
    target = root / path
    if target.is_dir():
        return len(list(target.rglob("*.md")))
    return 1 if target.is_file() else 0


def collect_rule_ids(root: Path) -> list[str]:
    ids: list[str] = []
    reference_dir = root / "docs/reference"
    if not reference_dir.is_dir():
        return ids
    for doc in sorted(reference_dir.glob("*.md")):
        try:
            ids.extend(RULE_ID_RE.findall(doc.read_text(encoding="utf-8")))
        except UnicodeDecodeError:
            continue
    return sorted(set(ids))


def collect_doc_statuses(root: Path) -> dict[str, str]:
    docs = root / "docs"
    if not docs.is_dir():
        return {}
    statuses: dict[str, str] = {}
    for doc in sorted(docs.rglob("*.md")):
        try:
            text = doc.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        match = STATUS_RE.search(text[:1200])
        if match:
            statuses[rel(doc, root)] = match.group(1).strip()
    return statuses


def collect_plan_statuses(root: Path) -> dict[str, list[str]]:
    plan_dir = root / "docs/planning"
    if not plan_dir.is_dir():
        return {}
    statuses: dict[str, list[str]] = {}
    for doc in sorted(plan_dir.glob("*.md")):
        try:
            text = doc.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        found = sorted(set(PLAN_STATUS_RE.findall(text)))
        if found:
            statuses[rel(doc, root)] = found
    return statuses


def classify(root: Path) -> str:
    docs = root / "docs"
    if not docs.exists() and not (root / "AGENTS.md").exists():
        return "new-or-undocumented"
    present = sum(1 for item in RECOMMENDED if (root / item).exists())
    if present < 4:
        return "partially-documented"
    if not (root / "docs/README.md").exists() or not (root / "docs/contributing/documentation.md").exists():
        return "mature-but-missing-entrypoints"
    return "mature"


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.exists():
        print(json.dumps({"error": f"Path does not exist: {root}"}, indent=2))
        return 2

    present = [item for item in RECOMMENDED if (root / item).exists()]
    missing = [item for item in RECOMMENDED if not (root / item).exists()]
    adr_dir = root / "docs/adr"
    adrs = sorted(path.name for path in adr_dir.glob("*.md") if ADR_RE.match(path.name)) if adr_dir.is_dir() else []

    result = {
        "root": str(root),
        "classification": classify(root),
        "present": present,
        "missing": missing,
        "markdownCounts": {item: count_markdown(root, item) for item in present},
        "adrFiles": adrs,
        "referenceRuleIds": collect_rule_ids(root),
        "documentStatuses": collect_doc_statuses(root),
        "planStatuses": collect_plan_statuses(root),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
