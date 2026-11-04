# External results

<!-- generated; ledger-sha256:1b027bc2fc9423795aad17a93e08dbc15f545bb228b530f3bab6e8501b7a037f; narrative-sha256:016720fbbc340bc7a1bb82e000674d685ffc19abccff52700675b2e360cc70c7; pr-status-sha256:73147d901817058603a949fd9455b5692d75f5aed43e4ce52f519674073cc9cc -->


Engineering outcomes tied to external evidence. A separate casebook for code, investigation, audits and arenas, keeping each kind of result distinct.

7 directly merged PRs; 3 contributions incorporated into merged maintainer fixes; 1 audit. 3 observations across 2 arenas/events, with Zoria counted once.

Public PRs in other owners' repositories: 99 submitted; 7 merged, 86 open, 6 closed without merge. GitHub snapshot: 2026-11-04 12:05 UTC. Own-repository and private activity is excluded.

[All PRs and current dispositions](PR_STATUS.en.md)

**2026-11-04 UTC** · [Українська](README.md) · [English](README.en.md)

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
