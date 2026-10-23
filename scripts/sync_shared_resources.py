#!/usr/bin/env python3
"""Maintain standalone skill packages; journal files are canonical for this list."""

import argparse
from pathlib import Path
import sys


SHARED_FILES = (
    "references/adjudication.md",
    "references/computational-ml.md",
    "references/domain-enrichment.md",
    "references/evaluation.md",
    "references/evaluation-key.md",
    "references/experimental-clinical.md",
    "references/peer-review-standards.md",
    "references/qualitative.md",
    "references/reviewer-methodology.md",
    "references/sources.md",
    "assets/domain-enrichment-prompt.md",
    "assets/evaluation-cases.jsonl",
    "assets/review-workbook.md",
    "assets/venue-scenarios.jsonl",
)


def synchronize(root: Path, write: bool = False) -> list[str]:
    source = root / "journal-peer-reviewer"
    target = root / "conference-peer-reviewer"
    # Read all sources first; a missing source must not cause a partial update.
    contents = {relative: (source / relative).read_bytes() for relative in SHARED_FILES}
    differences = []
    for relative, data in contents.items():
        destination = target / relative
        if not destination.is_file() or destination.read_bytes() != data:
            differences.append(relative)
    if write:
        for relative in differences:
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(contents[relative])
    return differences


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="report drift without writing (default)")
    mode.add_argument("--write", action="store_true", help="copy only listed shared resources")
    args = parser.parse_args()
    try:
        differences = synchronize(Path(__file__).resolve().parents[1], args.write)
    except OSError as exc:
        print(f"Shared resource error: {exc}", file=sys.stderr)
        return 2
    if differences:
        action = "Synchronized" if args.write else "Shared resource drift"
        print(f"{action}: {len(differences)} file(s)")
        for relative in differences:
            print(relative)
        return 0 if args.write else 1
    print("Shared resources match.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
