# ONNX IR · Dropout CSE

**Наш [#533](https://github.com/onnx/ir-py/pull/533) merged 2026-11-05T21:15:56Z через `justinchuby`.** [Merge commit](https://github.com/onnx/ir-py/commit/4b0302491a601f445e9035097d0b9f6f0f7f90fe) `4b0302491a601f445e9035097d0b9f6f0f7f90fe`; reviewed head `ab1253c9249eef26f48deb844e92ea66e9cebe31`.

## Проблема й рішення

CSE об’єднував незалежні standard-domain Dropout evaluations з однаковими входами. Їхні sampled masks ставали одним значенням, і downstream Xor перетворювався на Xor(v,v), тотожно false.

Dropout додано до наявного переліку nondeterministic exclusions. Регресія структурно зберігає два вузли й різні Xor operands, без вимоги, щоб дві випадкові маски обов’язково відрізнялися. Зайві thread-pool зміни тестового helper прибрані.

## Доказ і межі

Наш #533 злитий через justinchuby 05.11.2026 о 21:15:56 UTC, commit 4b0302491a601f445e9035097d0b9f6f0f7f90fe. Exact final head ab1253c9 містить лише exclusion і структурний test. Останній amendment документує 12 passing CSE methods; source/runtime proof вже виконаний раніше, під час підтримки книги його не повторювали.

Фінальний test будує валідну модель із двома training Dropout і downstream Xor. Full ONNX checker викликається до та після CSE; два Dropout і різні Xor inputs мають зберегтися. Він не порівнює випадково згенеровані маски. Зайві зміни thread-pool settings helper видалені; його original defaults збережені. Останній amendment документує 12 passing methods; повний hosted CI на amended head окремо цим записом не засвідчується.

Product tests, provider calls і повний runtime re-audit під час оновлення книги не запускалися. Merge - підтверджений зовнішній наслідок, не доказ universal coverage, production adoption, роботи чи оплати. Людина визначає напрям і відповідає за супровід; AI допомагає з дослідженням, реалізацією та перевіркою.

## English summary

CSE merged independent standard-domain Dropout evaluations with identical inputs. Their sampled masks became one value, turning downstream Xor into Xor(v,v), identically false.

Add Dropout to the existing nondeterministic exclusion. The regression structurally preserves two nodes and distinct Xor operands without requiring two random masks to differ. Unrelated thread-pool helper edits were removed.

Our #533 merged through justinchuby at 21:15:56 UTC on 5 November 2026, commit 4b0302491a601f445e9035097d0b9f6f0f7f90fe. Exact final head ab1253c9 contains only the exclusion and structural regression. The latest amendment documents 12 passing CSE methods; its previously executed source/runtime proof was not repeated during book maintenance.

Direct merge of our PR. Seeded and inference-mode Dropout remain conservatively excluded too. Final regression is structural, not an empirical random-mask inequality or universal stochastic-op proof. Latest 12-test execution is previously documented, not rerun for this book update; no full platform/performance claim. No product tests or provider calls were executed during this book refresh. These are separate outcomes from the earlier output-alias repair #521.
