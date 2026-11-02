# External results

<!-- generated; ledger-sha256:e40835983abddcb4f400bee44e4cc486d16165b97cbd06d7a4c54051cc01cd07; narrative-sha256:ca3bca8162d1d591bcc6ec4b662c919ea5c69935a179ff4abb19424c8f67b5f3 -->


Engineering outcomes tied to external evidence. A separate casebook for code, investigation, audits and arenas, keeping each kind of result distinct.

4 directly merged PRs; 2 contributions incorporated into merged maintainer fixes; 1 replacement still OPEN; 1 audit. 3 observations across 2 arenas/events, with Zoria counted once.

**2026-11-02 UTC** · [Українська](README.md) · [English](README.en.md)

## The book

[Українська PDF](book/pdf/external-results-uk.pdf) · [English PDF](book/pdf/external-results-en.pdf)

[Українська Markdown](book/uk/BOOK.md) · [English Markdown](book/en/BOOK.md)

[Results](RESULTS.en.md) · [Detailed bilingual cases](reports/README.md) · [Engineering](ENGINEERING.md)

## What the statuses mean

Merged means our PR was merged. Incorporated means a contribution to an accepted maintainer solution, not a merge of our patch. TVM-FFI remains an open maintainer replacement. Audits and competitions are separate; three competition records describe two events.

## How to append a result

1. Add a dated record and primary public source to [results.json](results.json).
2. Add a bilingual case in reports/ and a chapter in [book/narrative.json](book/narrative.json).
3. Run `python tools/build.py` (requires requirements.txt and DejaVu fonts).
4. Run `python tools/check.py` offline; inspect newly rendered PDF pages before publishing.

[Ledger schema and append contract](SCHEMA.md)

## Sources and reproducibility

`results.json` is the canonical status/date/source ledger. `book/narrative.json` owns authored narrative. Generated indices and books bind both source hashes. Detailed reports retain dated scope; the original M7 audit PDF is attached unchanged, not rewritten.

The check is offline and does not certify upstream CI, current live rankings or every claim in an attached historical audit. AI assistance is disclosed; no private work logs, model calls or personal biography are published.
