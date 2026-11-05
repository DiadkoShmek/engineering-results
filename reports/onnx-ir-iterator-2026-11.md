# ONNX IR · graph iterator

**Наш [#529](https://github.com/onnx/ir-py/pull/529) merged 2026-11-05T21:21:07Z через `justinchuby`.** [Merge commit](https://github.com/onnx/ir-py/commit/045f02a0dad7c8135305e4f5022784d4550d40e7) `045f02a0dad7c8135305e4f5022784d4550d40e7`; reviewed head `bbd36f8c808d55a1647d39bc2ab235c3b0b722de`.

## Проблема й рішення

Присвоєння finite iterator/generator у graph.inputs[:] або graph.outputs[:] спочатку витрачало його на ownership tracking, а потім передавало порожній iterable у list assignment. Clone міг втратити graph I/O, а extended slices - помилково відхиляти коректну довжину.

Заміна матеріалізується в tuple один раз до обох споживачів. Це узгоджено з constructor/extend pattern; ownership і Python slice semantics лишаються в наявному власнику.

## Доказ і межі

Наш #529 злитий через justinchuby 05.11.2026 о 21:21:07 UTC, commit 045f02a0dad7c8135305e4f5022784d4550d40e7. Фінальні два файли зберігають tuple snapshot і graph/model regressions. Історичний PR report має 760 tests/104 subtests та окремий 239/96 review; це не прогін під час цього оновлення книги.

Фінальні регресії охоплюють ordinary/extended/self slices, порожні заміни, ownership і clone-серіалізацію з full ONNX checker. 760 tests/104 subtests у початковому PR та 239 tests/96 subtests окремого review - історичні reports. Той review також описував multi-I/O Add/Sub models, ONNX validation, ORT CPU й NumPy reference. Тут це не видається за повторне виконання.

Product tests, provider calls і повний runtime re-audit під час оновлення книги не запускалися. Merge - підтверджений зовнішній наслідок, не доказ universal coverage, production adoption, роботи чи оплати. Людина визначає напрям і відповідає за супровід; AI допомагає з дослідженням, реалізацією та перевіркою.

## English summary

Assigning a finite iterator or generator to graph.inputs[:] or graph.outputs[:] consumed it for ownership tracking, then passed the exhausted iterable to list assignment. A clone could lose graph I/O, while valid extended slices could report a wrong size mismatch.

Materialize the replacement as a tuple once before either consumer, matching the existing constructor/extend pattern. Ownership and Python slice behavior remain in the existing container.

Our #529 merged through justinchuby at 21:21:07 UTC on 5 November 2026, commit 045f02a0dad7c8135305e4f5022784d4550d40e7. The final two-file patch retains the tuple snapshot and graph/model regressions. Historical PR reports list 760 tests/104 subtests and a separate 239/96 review; these were not rerun for this journal update.

Direct merge; finite supported iterable slice assignments. General rollback for invalid slice operations is unchanged. All runtime/test counts are historical PR reports, not new execution during book maintenance; no full repository/platform or deployment claim. No product tests or provider calls were executed during this book refresh. These are separate outcomes from the earlier output-alias repair #521.
