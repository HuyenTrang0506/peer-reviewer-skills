#!/usr/bin/env python3
"""Export canonical common resources into self-contained skill packages."""

import argparse
from pathlib import Path
import sys


SHARED_FILES = (
    "references/03-reporting/adjudication.md",
    "references/02-appraisal/computational-ml.md",
    "references/02-appraisal/domain-enrichment.md",
    "references/appendices/evaluation.md",
    "references/appendices/evaluation-key.md",
    "references/02-appraisal/experimental-clinical.md",
    "references/01-foundations/peer-review-standards.md",
    "references/02-appraisal/qualitative.md",
    "references/02-appraisal/reviewer-methodology.md",
    "references/01-foundations/rulebook.md",
    "references/appendices/sources.md",
    "references/02-appraisal/section-by-section.md",
    "references/02-appraisal/review-articles.md",
    "references/03-reporting/report-writing.md",
    "references/02-appraisal/figures-and-tables.md",
    "references/02-appraisal/language-and-readability.md",
    "references/03-reporting/professional-language.md",
    "references/01-foundations/integrity-and-overlap.md",
    "assets/domain-enrichment-prompt.md",
    "assets/evaluation-cases.jsonl",
    "assets/review-workbook.md",
    "assets/venue-scenarios.jsonl",
)

REVIEW_PACKAGES = ("journal-peer-reviewer", "conference-peer-reviewer")
LANGUAGE_SOURCE = "references/03-reporting/professional-language.md"


def synchronize(root: Path, write: bool = False) -> list[str]:
    source = root / "common"
    # Read all sources first; a missing source must not cause a partial update.
    contents = {relative: (source / relative).read_bytes() for relative in SHARED_FILES}
    exports = {
        f"{package}/{relative}": data
        for package in REVIEW_PACKAGES
        for relative, data in contents.items()
    }
    exports["professional-office-language/references/professional-language.md"] = contents[
        LANGUAGE_SOURCE
    ]
    differences = []
    for relative, data in exports.items():
        destination = root / relative
        if not destination.is_file() or destination.read_bytes() != data:
            differences.append(relative)
    if write:
        for relative in differences:
            destination = root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(exports[relative])
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
