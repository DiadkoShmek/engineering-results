# External results

<!-- generated; ledger-sha256:01e1c97b07fc337e3b63a7e70911afad55c63a88a0c7a43b67c664eeb218abd4; narrative-sha256:d2dd325e8e8ab4f4a6b9a81fdb55e325b1b93f482a6ea60b3a1324dbf27e4cbe; pr-status-sha256:6cf76b0331c7751ed6b38b31ea7bb4b5800e5b141777137a1863ab267eb56d11 -->


Engineering outcomes tied to external evidence. A separate casebook for code, investigation, audits and arenas, keeping each kind of result distinct.

13 directly merged PRs; 4 contributions incorporated into merged maintainer fixes; 1 audit. 3 observations across 2 arenas/events, with Zoria counted once.

Public PRs in other owners' repositories: 134 submitted; 13 merged, 113 open, 8 closed without merge. GitHub snapshot: 2026-11-05 21:47 UTC. Own-repository and private activity is excluded.

[All PRs and current dispositions](PR_STATUS.en.md)

**2026-11-05 UTC** · [Українська](README.md) · [English](README.en.md)

## The book

[Українська PDF](book/pdf/external-results-uk.pdf) · [English PDF](book/pdf/external-results-en.pdf)

[Українська Markdown](book/uk/BOOK.md) · [English Markdown](book/en/BOOK.md)

[Results](RESULTS.en.md) · [Detailed bilingual cases](reports/README.md) · [Engineering](ENGINEERING.md)

## What the statuses mean

Merged means our PR was merged. Incorporated means a contribution to an accepted maintainer solution, not a merge of our patch. Open maintainer replacements are recorded as pending. Audits and competitions are separate; three competition records describe two events.

## How to append a result

1. Add a dated record and primary public source to [results.json](results.json).
2. Add a bilingual case in reports/ and a chapter in [book/narrative.json](book/narrative.json).
3. Run `python tools/build.py` (requires requirements.txt and DejaVu fonts).
4. Run `python tools/check.py` offline; inspect newly rendered PDF pages before publishing.

[Ledger schema and append contract](SCHEMA.md)

## Sources and reproducibility

`results.json` owns confirmed outcomes, `book/narrative.json` authored narrative, and `pr-status.json` the dated inventory of all external PRs. Generated indices and books bind all three sources. Detailed reports retain dated scope; the original M7 audit PDF is attached unchanged.

The check is offline and does not certify upstream CI, current live rankings or every claim in an attached historical audit. AI assistance is disclosed; no private work logs, model calls or personal biography are published.
