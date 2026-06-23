#!/usr/bin/env python3
"""Inventory standard repository documentation paths.

This script is read-only. It prints JSON so an agent can route to the smallest
useful docs set without loading every document into context.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


STANDARD_FILES = [
    "AGENTS.md",
    "docs/README.md",
    "docs/contributing/documentation.md",
    "docs/contributing/cross-cutting-concerns.md",
    "docs/product/vision.md",
    "docs/planning/roadmap.md",
    "docs/planning/implementation-status.md",
]

STANDARD_DIRS = [
    "docs/architecture",
    "docs/reference",
    "docs/adr",
]

RULE_ID_RE = re.compile(r"Rule ID:\s*`([^`]+)`")


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def collect_rule_ids(root: Path) -> list[str]:
    ids: list[str] = []
    reference_dir = root / "docs/reference"
    if not reference_dir.exists():
        return ids

    for doc in sorted(reference_dir.glob("*.md")):
        try:
            text = doc.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        ids.extend(RULE_ID_RE.findall(text))
    return sorted(set(ids))


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.exists():
        print(json.dumps({"error": f"Path does not exist: {root}"}, indent=2))
        return 2

    files = [path for item in STANDARD_FILES if (path := root / item).is_file()]
    dirs = [path for item in STANDARD_DIRS if (path := root / item).is_dir()]

    docs_dir = root / "docs"
    markdown_docs = sorted(rel(path, root) for path in docs_dir.rglob("*.md")) if docs_dir.is_dir() else []

    result = {
        "root": str(root),
        "standardFiles": [rel(path, root) for path in files],
        "standardDirs": [rel(path, root) for path in dirs],
        "markdownDocs": markdown_docs,
        "referenceRuleIds": collect_rule_ids(root),
        "missingRecommended": [
            item
            for item in [*STANDARD_FILES, *STANDARD_DIRS]
            if not (root / item).exists()
        ],
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
