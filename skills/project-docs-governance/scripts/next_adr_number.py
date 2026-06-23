#!/usr/bin/env python3
"""Print the next ADR number for a repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ADR_RE = re.compile(r"^(\d{4})-.+\.md$")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    adr_dir = root / "docs/adr"
    numbers = []
    if adr_dir.is_dir():
        for path in adr_dir.glob("*.md"):
            match = ADR_RE.match(path.name)
            if match:
                numbers.append(int(match.group(1)))
    print(f"{(max(numbers) + 1) if numbers else 1:04d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
