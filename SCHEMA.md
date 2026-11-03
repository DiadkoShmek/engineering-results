# Ledger and append contract

`results.json` owns status, dates, primary URLs, authorship disposition and evidence identity. `book/narrative.json` owns bilingual engineering narrative and references record IDs. `pr-status.json` owns a dated, fully paginated inventory of authored PRs in other owners' repositories. Generated Markdown/PDF outputs are not the source of any of these three inputs.

Each record needs a stable unique `id`, `category`, `format`, `status`, `as_of`, `source_url`, and a truthful `boundary`. Use `project` for engineering cases or `competition` for events. Add `report_path` when a detailed report exists.

- `merged`: our contribution is merged; require `contribution_merged: true` and the merge commit.
- `incorporated_in_maintainer_fix`: our proposal was not merged; require `contribution_merged: false` and merged `upstream_fixes` with commit identities.
- `superseded_by_open_maintainer_fix`: our proposal was not merged and the linked replacement is still OPEN with `merged: false`. Never add it to directly merged totals.
- `credited_in_release`: an external audit/triage outcome; implementation authorship remains separate.
- `snapshot`, `preliminary`, `final`: competition observations with their original scope and dated sources. They are not PR merges.

Competition identity currently uses the exact stable `competition` name. Historical and final observations of the same event must share that name. An added observation increases record count, not event count. A final announcement does not establish an exact rank or payment unless the source does.

`as_of` is the source record's calendar date. Preserve `display_timezone`, `date_basis`, `observed_at` and `checked_at` where present. Precise timestamps use ISO 8601 UTC (`Z`); do not relabel a historical local date as a UTC event date. Merge timestamps and observation dates are distinct.

Evidence uses a relative repository `path` and SHA-256. Keep an original attached audit unchanged; add dated follow-up rather than rewrite its history. Private logs, machine paths, credentials and unpublished operational identities do not belong here.

To append: add the record, public detailed bilingual report, and narrative chapter/reference. Run `python tools/build.py`, then `python tools/check.py`. The latter validates state invariants, a deliberately corrupted pending-merge control, chapter coverage, local links/anchors, evidence hashes and a bounded privacy scan. It is offline and cannot certify live upstream status or all CI. Visually inspect new PDF pages after a meaningful content/layout change.

PDF builds require Python 3.12+, `requirements.txt`, and DejaVu fonts (`DEJAVU_DIR` can select the font directory). The check uses the Python standard library. Keep final QA manifests outside this public repository using `--manifest`.

## PR snapshot

Keep `pr-status.json` separate from accepted-result records. OPEN and CLOSED rows never become direct merges without a merge timestamp and merge commit. A closed superseded proposal may also be an incorporated outcome in `results.json`; that does not change the PR state. Own-repository PRs are explicitly excluded from the external denominator. Every merged row must correspond one-for-one to a direct-merge ledger record; the validator compares identities and commits, not just totals.

All rows and generated counts are dated. Selected review signals carry their own checked-at timestamps; they do not certify the other PRs' CI or forecast a merge. Refresh the complete API inventory, append newly confirmed outcomes and narratives, then rebuild both languages. Featured submitted cases must still be OPEN. The offline check rejects inconsistent counts, an invented merge, stale source hashes and mismatches between the merge ledger and PR inventory.
