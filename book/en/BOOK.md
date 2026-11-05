# External results

<!-- generated; ledger-sha256:c28a069b22b49e30cfcaf845733b0343f5cbb9e41680f977ebbe723440bbb60a; narrative-sha256:67b52d20ff53a725d7394fa27e3d4a1f3f7b3278503d9d981f515da6877bc9ea; pr-status-sha256:44941cfd85d7964e37323bbd0017d2600e85379c19c7836a6a8f877b1bd6b45f -->


DiadkoShmek · 2026-11-05 UTC

## Role and evidence

I investigate failures, define contracts and verify consequences. AI tools assist research, implementation and checking; I set direction, take responsibility for engineering decisions and authorize external actions. This book does not measure autonomy percentages or rank AI models.

10 directly merged PRs; 4 contributions incorporated into merged maintainer fixes; 1 audit. 3 observations across 2 arenas/events, with Zoria counted once.

Public PRs in other owners' repositories: 134 submitted; 10 merged, 116 open, 8 closed without merge. GitHub snapshot: 2026-11-05 19:07 UTC. Own-repository and private activity is excluded.

[Complete PR status](../../PR_STATUS.en.md)

Every status and date below comes from results.json. A local PASS, external credit and a merge are different claims. The preliminary and final Zoria records belong to one event.

## Contents

1. [Instructor](#case-instructor)

2. [PyLops](#case-pylops)

3. [Redis Python client](#case-redis-monitor)

4. [Microsoft Semantic Kernel](#case-semantic-kernel)

5. [ONNX Range](#case-onnx-range)

6. [ONNX IR](#case-onnx-ir)

7. [FilesDrop](#case-filesdrop)

8. [Prime Intellect](#case-prime)

9. [M7 MCP](#case-m7)

10. [Braintrust SDK JavaScript](#case-braintrust)

11. [Kraft](#case-kraft)

12. [PyTorch TensorDict](#case-tensordict)

13. [BlackJAX](#case-blackjax)

14. [TensorLy](#case-tensorly)

15. [Apache TVM-FFI](#case-tvm)

16. [CodinGame - Mad Pod Racing](#case-codingame)

17. [Zoria 2026 / UA SKILLS](#case-zoria)

<a id="case-instructor"></a>

## 01. Instructor

**2026-11-05 · Incorporated into a merged maintainer fix**

Our #2866 closed unmerged; maintainer consolidation #2899 merged with an explicit reference to our PR. The reviewed head retains our coauthor trailer, but the final squash commit does not. Source comparison was performed; the maintainer-reported 101 passing tests were not rerun for this journal update. No provider, deployment or live-service proof.

### Problem

The partial-JSON streaming sanitizer removed DEL/C1 even inside valid strings, changing keys and values before completed validation.

### My decision and the external choice

Our #2866 narrowed the regex to C0 and added Unicode streaming regressions. The maintainer consolidated it with other proposals in #2899, using per-stream quote/escape tracking to preserve DEL/C1 inside JSON strings while retaining historical repair outside strings.

### Validation and limits

Native GitHub confirms #2899 merged through jxnl-oai at 18:47:01 UTC on 5 November 2026, commit 5f352b0085fb2f8adaa26d69a6447ed5cabd2034. Head 723629d57c05edb996db411e93e7b37ae5c95a8b matches the source-audited head: the C0-only return AST is retained and sync/async tests are expanded. The 101 passing tests are the maintainer’s report and were not rerun for this journal update.

### What I carry forward

An original PR and a merged maintainer consolidation are distinct outcomes. Check attribution on both the reviewed head and final squash: a trailer can disappear while the explicit PR reference survives.

- [Primary source](https://github.com/567-labs/instructor/pull/2899)

- [Our proposal](https://github.com/567-labs/instructor/pull/2866)

- [Acknowledgement](https://github.com/567-labs/instructor/pull/2866#issuecomment-6663590222)

[Повний кейс / Full report](../../reports/instructor-2026-11.md)

<a id="case-pylops"></a>

## 02. PyLops

**2026-11-04 · Direct PR merged · UTC 2026-11-04T21:44:06.308045+00:00 · 2026-11-04T21:34:47Z**

One-dimensional real nonstationary dense operator orientation; prior runtime proof not rerun for journal update. Multidimensional dense-shape/complex-filter limitations remain; no production adoption or income claim.

### Problem

The dense matrix of a one-dimensional nonstationary convolution stored impulse responses as rows rather than columns. Dense multiplication and direct inversion disagreed with the public operator even for varying symmetric filters.

### My decision and the external choice

The contribution transposes the assembled matrix and adds forward/adjoint equivalence assertions to an existing seeded test. Matteo Ravasi rearranged the assertions around Cdense before merging; the production correction is unchanged.

### Validation and limits

Native GitHub confirms direct merge #837 at 21:34:47 UTC on 4 November 2026. The PR documents 18 nonstationary-module passes, 543 neighboring passes/3 skips, 128 coordinate-oracle matrices and 48 operator-action cases. A concrete 51-sample inverse fixture improves relative error from 8.24% to below 2e-16. Runtime checks were not repeated for this journal update.

### What I carry forward

An operator matrix must reproduce its action on coordinate impulses. Testing both forward and adjoint separates an orientation bug from an accidentally symmetric control.

- [Primary source](https://github.com/PyLops/pylops/pull/837)

[Повний кейс / Full report](../../reports/pylops-2026-11.md)

<a id="case-redis-monitor"></a>

## 03. Redis Python client

**2026-11-04 · Direct PR merged · UTC 2026-11-04T16:20:18.445505Z · 2026-11-04T15:44:00Z**

Focused MONITOR lifecycle change; no full replica/sentinel/cluster/Stack/TLS/Enterprise validation claim. Prior local tests are reported separately from the newly verified upstream merge.

### Problem

When MONITOR context entry failed, Python did not call exit and the borrowed connection remained checked out. A max_connections=1 pool could stop serving even PING; async setup also has a cancellation path.

### My decision and the external choice

Sync/async MONITOR clean up failed entry, detach the connection before exit cleanup and return it to the pool in finally. Async release remains shielded. Review follow-up removed extra exception-precedence branches and permutations while retaining the requested maintainer shape.

### Validation and limits

The PR records a temporary loopback Redis 8.0.2 run: 23 passing tests and three native skips for each of RESP2 and RESP3, including ACL denial, single-connection pool reuse and async cancellation. GitHub confirms the direct merge of #4550. The server was not restarted for this journal update.

### What I carry forward

Failed context entry does not automatically invoke exit. The owner of a borrowed resource must restore the pool explicitly and verify recovery with an actual subsequent command.

- [Primary source](https://github.com/redis/redis-py/pull/4550)

[Повний кейс / Full report](../../reports/redis-monitor-2026-11.md)

<a id="case-semantic-kernel"></a>

## 04. Microsoft Semantic Kernel

**2026-11-04 · Direct PR merged · UTC 2026-11-04T16:20:18.445505Z · 2026-11-04T14:46:53Z**

Native-generator invocation cleanup only; separate prompt/provider forwarding layers and full SDK integration matrix are not established. Merge metadata refreshed; runtime tests not rerun.

### Problem

After early closure or cancellation of a streaming invocation, the underlying sync/async Python generator remained suspended. Its finally block did not release resources when the invocation ended; retaining the generator makes this independent of garbage collection.

### My decision and the external choice

The contribution wraps actual native generators in closing/aclosing and closes the owned function-invocation stream in Kernel.invoke_stream. Ordinary values and custom close-bearing results retain their existing behavior; public signatures are unchanged.

### Validation and limits

The public PR records eight failing and 148 passing baseline tests versus 156 passing candidate tests, 18 added retained-generator scenarios and separate cancellation checks. GitHub confirms the direct merge of #14701. Runtime tests were not repeated for this journal update.

### What I carry forward

The layer that owns a created stream must finalize it. Retaining the source in the regression distinguishes explicit cleanup from incidental garbage collection.

- [Primary source](https://github.com/microsoft/semantic-kernel/pull/14701)

[Повний кейс / Full report](../../reports/semantic-kernel-2026-11.md)

<a id="case-onnx-range"></a>

## 05. ONNX Range

**2026-11-04 · Direct PR merged · 2026-11-04T01:09:20Z**

Direct merge of integer Range shape-inference fix; upstream APPROVED reviews are recorded separately. Runtime tests were not rerun for this book refresh, and production use is not established.

### Problem

Integer Range shape inference subtracted start from limit in the signed input type before conversion to floating point. For INT32 from −2147483648 to 2147483647 with step 2147483647, overflow produced zero instead of three; floating-point division can also round an INT64 quotient across a ceiling boundary.

### My decision and the external choice

A shared helper for both historical schemas computes unsigned distance and step magnitude, then exact integer ceiling division. It supports both directions and the minimum negative step; the floating-point path is unchanged.

### Validation and limits

GitHub confirms the direct merge of PR #8734 on 4 November 2026 and its merge commit. The PR description documents the example and approach; runtime tests were not rerun for the book refresh.

### What I carry forward

For a discrete element count, exact integer arithmetic with a safely represented distance avoids both signed subtraction overflow and quotient rounding errors.

- [Primary source](https://github.com/onnx/onnx/pull/8734)

[Повний кейс / Full report](../../reports/onnx-range-2026-11.md)

<a id="case-onnx-ir"></a>

## 06. ONNX IR

**2026-11-03 · Direct PR merged · UTC 2026-11-03T17:33:18.542858Z · 2026-11-03T16:40:54Z**

Merged public-output alias preservation fix. Previously recorded focused CPU checks cover named outputs and ownership; they were not rerun for this journal refresh. The full nox/Python/Torch/GPU matrix and production deployment are not established.

### Problem

In y = Relu(x), z = Identity(y), both y and z are public outputs. Eliminating the Identity renamed the first output to z, leaving two z outputs. Requests for the original y name then became invalid even though local graph checks could pass.

### My decision and the external choice

Retain an output Identity when its input is already a public output or belongs to an outer graph. The latter guard prevents captured parent values from being renamed or adopted as direct subgraph outputs. Safe internal aliases can still be eliminated.

### Validation and limits

The submitted PR records 28 focused tests and nine subtests, named-output checks through ONNX ReferenceEvaluator and ONNX Runtime CPU, and a NumPy oracle. Prepublication AI review checked 23 additional cases and exposed the need to protect parent-value ownership. Runtime tests were not repeated for this book refresh; GitHub supplied the merge commit and timestamp.

### What I carry forward

Graph optimization must preserve public names and value ownership as well as numerical results.

- [Primary source](https://github.com/onnx/ir-py/pull/521)

[Повний кейс / Full report](../../reports/onnx-ir-2026-11.md)

<a id="case-filesdrop"></a>

## 07. FilesDrop

**2026-10-21 · Direct PR merged**

Merged API fixes with local regression coverage; no production deployment, live service test or payment claimed.

### Problem

I started from two lifecycle failures: failed deletion could disappear from the next cleanup batch, and a deadline did not end waiting for DNS. The first problem was loss of retryable work; the second was the boundary between request waiting and the native resolver.

### My decision and the external choice

I retained failed items for another pass and committed successful deletions separately. A 501-file counterexample exposed starvation behind one persistent failure. For URL uploads, cancellation ends request waiting while retaining address validation and redirect behavior.

### Validation and limits

The regressions first failed on the base. The saved local run passed 236 tests across 12 API suites. Temporary files and DNS/HTTP doubles exercised the intended transitions, rather than a production deployment.

### What I carry forward

Cleanup must preserve retryability. Cancelling a wait does not imply stopping the underlying system operation.

- [Primary source](https://github.com/AndreyBegma/FilesDrop/pull/32)

[Повний кейс / Full report](../../reports/filesdrop-2026-10.md)

<a id="case-prime"></a>

## 08. Prime Intellect

**2026-10-24 · Incorporated into a merged maintainer fix**

Maintainer credits our reproduction and investigation. Our proposed patch was superseded, not merged; the original issue was filed by another contributor. No employment or payment claimed.

### Problem

I investigated how model and client configuration inherit shared sampling parameters. Another contributor had already opened the original issue. My role was to turn that report into an executable contract and a clear reproducer.

### My decision and the external choice

I proposed a boundary around explicit model/client overrides. The maintainer instead chose the client boundary: another model on the same server retains shared parameters, while a separate client gets its own. This is a different implementation and a refined contract, not a merge of my patch.

### Validation and limits

My proposed-contract matrix moved from 11 failing and seven passing scenarios to 18 passing. Those are scenarios, not distinct defects. The maintainer separately credited the reproduction and investigation. These tests did not establish live inference or training behavior.

### What I carry forward

A contribution can shape a maintainer decision even when the proposed patch is not the accepted code.

- [Primary source](https://github.com/PrimeIntellect-ai/verifiers/pull/2925#issuecomment-6385135636)

- [Our proposal](https://github.com/PrimeIntellect-ai/verifiers/pull/2925)

- [Maintainer implementation](https://github.com/PrimeIntellect-ai/verifiers/pull/2973)

- [Maintainer implementation](https://github.com/PrimeIntellect-ai/prime-rl/pull/4243)

[Повний кейс / Full report](../../reports/prime-intellect-2026-10.md)

<a id="case-m7"></a>

## 09. M7 MCP

**2026-10-29 · Audit credited in release**

Public review/triage attribution and maintainer maintenance release. Audit groups and maintainer registry entries are not interchangeable. Focused follow-up retained unresolved error paths; no live model or IDE evaluation.

### Problem

I reviewed a specific MCP-server snapshot: phase transitions, repeated calls, state persistence and handoff. The audit required separating contract defects from observer mistakes and environment limitations.

### My decision and the external choice

I documented reproducible observations with inputs, causes and limits. Maintainers built their own issue registry and implemented the first maintenance release. Their registry entries are not a one-to-one copy of the audit groups.

### Validation and limits

The original public PDF is retained unchanged rather than rewritten around a later release. A focused follow-up on a pinned commit passed 168 tests and an SDK stdio check while retaining three unresolved error paths. It was not a complete reaudit.

### What I carry forward

An audit should leave a checkable route to each failure and retain what a later release has not established.

- [Primary source](https://github.com/DukeDeSouth/m7-mcp-oss/releases/tag/v3.18.1)

[Повний кейс / Full report](../../reports/m7-2026-10.md)

<a id="case-braintrust"></a>

## 10. Braintrust SDK JavaScript

**2026-11-02 · Direct PR merged · 2026-11-02T11:37:30Z**

Merged streaming UTF-8 logging fix with local regression coverage; no full monorepo, browser or real-provider end-to-end claim.

### Problem

The failure occurred at logging chunk boundaries: a multibyte UTF-8 character can span two byte chunks. Correct text should not depend on how a transport partitions its stream.

### My decision and the external choice

I retained decoder state between reads and separated final flushing from intermediate chunks. Testing every byte boundary made the invariant concrete: different partitions of one byte stream must produce the same text.

### Validation and limits

The first focused run had six failures and 13 passing controls. Related suites passed 178 tests on both tested Node versions. These are local checks of selected paths, not the entire monorepo, browser execution or a real-provider end-to-end test.

### What I carry forward

Chunk boundaries belong to the transport. Decoder state must belong to the complete logical stream.

- [Primary source](https://github.com/braintrustdata/braintrust-sdk-javascript/pull/2701)

[Повний кейс / Full report](../../reports/braintrust-2026-11.md)

<a id="case-kraft"></a>

## 11. Kraft

**2026-11-02 · Direct PR merged · 2026-11-02T12:08:30Z**

Merged repeatable user-scope initialization fix. Tests used a Claude subprocess double, without live agent calls or user-configuration changes.

### Problem

Repeated user-scope initialization detected an existing MCP registration and returned before refreshing skills. The command appeared repeatable, but its second responsibility was skipped.

### My decision and the external choice

I separated a successfully existing registration from a genuine subprocess failure. The former allows skill refresh to proceed; the latter must stop before writes. The change repairs control flow without invoking a live agent.

### Validation and limits

The focused suite passed 16 tests. Repository ci-checks and mutation checks exercised the distinction between branches. The Claude subprocess was a test double; those checks did not change user configuration or call an external agent.

### What I carry forward

Repeated initialization should repeat useful work rather than mistake an idempotent state for failure.

- [Primary source](https://github.com/itsOmidKarami/kraft/pull/1227)

[Повний кейс / Full report](../../reports/kraft-2026-11.md)

<a id="case-tensordict"></a>

## 12. PyTorch TensorDict

**2026-11-01 · Incorporated into a merged maintainer fix**

Maintainer credits the earlier proposed fix, report and thorough tests. Our PR #3426 was superseded, not merged; the smaller accepted implementation is the maintainer's.

### Problem

A partial checkpoint in a nested TensorDictParams could fail despite strict=False. I examined missing keys, nesting, assignment and pre-hooks: behavior that PyTorch users already rely on.

### My decision and the external choice

I proposed a loader repair and differential controls against native nn.Module. The maintainer chose a smaller owner-level change: delegate to PyTorch rather than maintain a copy. The public credit covers the earlier fix, report and thorough tests.

### Validation and limits

Our candidate had 44 failing scenarios and four passing controls on the base; its focused suites then passed 251 tests with two CUDA skips. Those counts do not describe the maintainer implementation, whose acceptance is recorded by a separate upstream PR.

### What I carry forward

When a lower layer already owns the contract, delegation can be stronger than a more accurate copy.

- [Primary source](https://github.com/pytorch/tensordict/pull/3427)

- [Our proposal](https://github.com/pytorch/tensordict/pull/3426)

- [Acknowledgement](https://github.com/pytorch/tensordict/pull/3426#issuecomment-6563347852)

[Повний кейс / Full report](../../reports/tensordict-2026-11.md)

<a id="case-blackjax"></a>

## 13. BlackJAX

**2026-11-02 · Direct PR merged · 2026-11-02T14:43:52Z**

Merged Barker MCMC numerical-stability fix with CPU differential checks. Full suite not run; unchanged GIST CI failure reproduced on exact base and head. No GPU/TPU or performance claim.

### Problem

Barker MCMC could reject an improving move because an intermediate exp overflowed. The final log expression remained mathematically finite, but direct evaluation lost it.

### My decision and the external choice

I replaced unstable log(1+exp(x)) evaluation with standard softplus. The important proof was not merely absence of inf, but the correct proposal probability against an independent density calculation. Ordinary inputs remained controls.

### Validation and limits

Across 768 CPU steps, the NumPy oracle found 142 base mismatches and none after the change; all 384 ordinary controls already passed. The full suite was not run. An unchanged GIST CI failure was reproduced on base and head; no GPU, TPU or speed-up is claimed.

### What I carry forward

Stabilize the intermediate computation while preserving the mathematical quantity and control regimes.

- [Primary source](https://github.com/blackjax-devs/blackjax/pull/1068)

[Повний кейс / Full report](../../reports/blackjax-2026-11.md)

<a id="case-tensorly"></a>

## 14. TensorLy

**2026-11-03 · Direct PR merged · 2026-11-02T23:54:45Z**

Our PR merged. The compact regression and two relevant modules were checked on CPU with NumPy/PyTorch and core/einsum (70 tests per run). The full repository, GPU and remaining backend/version matrix were not run; the earlier large oracle campaign was not repeated for the test-only revision.

### Problem

A single-factor Khatri-Rao product returned its matrix before applying optional column weights and a row mask. The same path can remain after skip_matrix, silently violating the operation contract and affecting weighted CP gradients.

### My decision and the external choice

Both tenalg implementations now apply weights and mask before returning the single factor. Following JeanKossaifi’s review, added coverage was reduced to one compact regression with literal expected values. The maintainer merged our PR rather than replacing it with a different implementation.

### Validation and limits

For matrix [[1,2,3],[4,5,6]], weights [2,0,-1] and mask [0,2], the expected output is [[0,0,0],[16,0,-12]]. The regression fails on the exact base across NumPy/PyTorch and core/einsum and catches independently dropping weights or mask. Before submission, both relevant modules passed 70 tests in each mode; Black checked 156 files. No runtime tests were repeated merely to record the merge.

### What I carry forward

One carefully chosen example can cover both required multipliers without a grid of near-duplicate tests. The maintainer’s request for simpler coverage became part of the accepted contribution.

- [Primary source](https://github.com/tensorly/tensorly/pull/695)

- [Acknowledgement](https://github.com/tensorly/tensorly/pull/695#issuecomment-6591551013)

[Повний кейс / Full report](../../reports/tensorly-2026-11.md)

<a id="case-tvm"></a>

## 15. Apache TVM-FFI

**2026-11-03 · Incorporated into a merged maintainer fix**

Our PR #897 was superseded, not merged. The publicly linked maintainer replacement #898 merged, changing short moved-string construction instead of transplanting our hashing patch. The replacement and all explicit external-heap scenarios were not runtime-retested for this record.

### Problem

Equal short byte values with inline and heap storage received different structural hashes, violating expectations of StructuralKey cache lookup and native map deduplication. My proposed patch repaired both hashing paths.

### My decision and the external choice

The maintainer publicly linked the proposal to a successor and chose another layer: a short moved std::string directly constructs inline String/Bytes. The changed file sets are disjoint; no direct patch transplant was found in the inspected diffs. Successor PR #898 merged on 2 November 2026 at 22:16:16 UTC; our proposal remains superseded.

### Validation and limits

Native PR states, chronology, commits and diffs were compared. The constructor-side change removes the producer path used by the original reproducer. The successor and all explicit external-heap cases were not runtime-retested for this record.

### What I carry forward

A reproduction can lead to another repair. Superseded and merged are different external outcomes.

- [Primary source](https://github.com/apache/tvm-ffi/pull/898)

- [Our proposal](https://github.com/apache/tvm-ffi/pull/897)

- [Acknowledgement](https://github.com/apache/tvm-ffi/pull/897#issuecomment-6588300834)

[Повний кейс / Full report](../../reports/tvm-ffi-2026-11.md)

<a id="case-codingame"></a>

## 16. CodinGame - Mad Pod Racing

**2026-10-21 (Europe/Helsinki) · Dated arena snapshot · UTC 2026-10-20T22:06:15.975Z · 86/1657 (Legend League)**

Dated league ranking snapshot, not a final tournament result or an all-time best.

### Problem

I developed a bot for a continuous arena, where a local win does not establish an external rank. The record preserves two experiments: early rejection of a hypothesis and a conditional local candidate after criteria changed.

### My decision and the external choice

V79 stopped after two wins in eight completed games because the required threshold was no longer reachable. V89b recorded 221/400, but criteria changed after earlier failures, so I do not treat it as an independent clean win or an officially submitted version.

### Validation and limits

The external league snapshot has its own public source and dated screenshot. The local extract omits candidate code, referee and full traces; hashes alone cannot reproduce the matches or independently attest to their contents.

### What I carry forward

A stopping rule protects against proving a desired outcome. Local experiments and external arenas have different units of evidence.

- [Primary source](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing)

- [Arena profile](https://www.codingame.com/profile/effff781bd270b96c3fddbba39a29b4a7099847)

<a id="case-zoria"></a>

## 17. Zoria 2026 / UA SKILLS

**2026-10-19 (Europe/Helsinki) · Historical preliminary result · UTC 2026-10-20T22:06:05.463Z · 5/9 (overall preliminary score of second-stage participants)**

Public table excludes episode R3; no final placement, award or payment claimed.

**2026-10-27 (Europe/Helsinki) · Season prize winner; exact rank not established**

Organizer names this account among five prize winners. This record does not establish an exact final rank, a ranked participant count or payment.

### Problem

This case retains two observations of one tournament. A preliminary second-stage table and a later organizer announcement describe different levels of completion. I do not count them as independent tournament outcomes.

### My decision and the external choice

My engineering role was development and validation of my bot and preservation of external evidence boundaries. A code-level engineering report is not yet public, so this book does not invent algorithm or autonomy claims.

### Validation and limits

The preliminary table excluded R3. The organizer later named the account among prize winners. The date the announcement was checked is not its publication date; exact final placement and payment are not established here.

### What I carry forward

History should retain a preliminary state without turning it into another victory.

- [Primary source](https://zoria.net/news/#19102026-попередній-підсумок-другого-етапу)

- [Primary source](https://ua.linkedin.com/company/ua-skills)

## How this book grows

For each new result I retain the UTC observation date, my role, primary source and exact external disposition. Old reproductions remain dated; a follow-up is not a complete reaudit. I append results.json, add narrative to book/narrative.json and run the build and offline check.
