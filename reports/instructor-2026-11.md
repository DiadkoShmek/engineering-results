# Instructor · Unicode у частковому streaming JSON

**05.11.2026: наша пропозиція #2866 закрита без merge; консолідація мейнтейнера #2899 злита.** Це четвертий внесок у merged-рішення мейнтейнера; кількість власних direct merges лишається 10.

Наш [#2866](https://github.com/567-labs/instructor/pull/2866) показав, що sanitizer видаляє JSON-valid DEL/C1 із рядкових значень. Пропозиція звужувала regex до C0 й додавала Unicode streaming regressions. Мейнтейнер `jxnl-oai` [закрив його як консолідований](https://github.com/567-labs/instructor/pull/2866#issuecomment-6663590222) о 16:40:27 UTC.

У [#2899](https://github.com/567-labs/instructor/pull/2899) той самий C0-only return expression збережений на рівні AST. Новий per-stream sanitizer відстежує лапки та backslash escapes між chunks: DEL/C1 лишається всередині JSON-рядків, а історичне виправлення malformed controls поза рядками зберігається. Sync та async мають окремий sanitizer для кожного stream. Початкові вісім regression cases переписані й розширені до sync/async × literal/escaped × whole/one-/three-character chunks, з перевіркою ключів і значень. Окремі тести покривають outside-string repair, nesting/escapes, C0, unfinished streams та state isolation.

## Злиття й точна атрибуція

- Під час першого source audit #2899 ще був OPEN. Цей історичний стан не був merge.
- Злиття підтверджено 05.11.2026 о 18:47:01 UTC через `jxnl-oai`: [commit 5f352b0](https://github.com/567-labs/instructor/commit/5f352b0085fb2f8adaa26d69a6447ed5cabd2034).
- Head `723629d57c05edb996db411e93e7b37ae5c95a8b` збігається з незалежно перевіреним source audit.
- Опис #2899 та фінальний squash commit прямо вказують `Consolidates #2842, #2866, #2893`.
- Reviewed head містить наш coauthor trailer. У фінальному squash commit цей trailer **відсутній**. Запис не приписує нам фінальну Git coauthor-атрибуцію, якої там немає.

Source comparison звірив п’ять exact-head файлів із Git blob SHA та описав перенесену причину й розширення мейнтейнера. **101 passing tests — твердження мейнтейнера в PR**, а не повторний локальний прогін цього оновлення. Продуктові тести й provider calls під час підтримки книги не запускалися. Production deployment не встановлено.

Це прийняте продовження нашого finding, запропонованого fix і regressions у ширшій реалізації мейнтейнера. Наш PR не став прямим merge; нове подання або merge до закритого проходу 35 не додається. Людина задає напрям, володіє поданням і відповідає за супровід; AI допомагає з дослідженням, реалізацією та перевіркою.

## English summary

Our [#2866](https://github.com/567-labs/instructor/pull/2866) proposed preserving valid Unicode in partial streaming JSON by restricting sanitizer removal to C0, with Unicode regressions. It closed unmerged at 16:40:27 UTC on 5 November 2026, explicitly consolidated into maintainer `jxnl-oai`’s [#2899](https://github.com/567-labs/instructor/pull/2899).

The replacement retains the original C0-only return-expression AST and adds per-stream quote/escape tracking. DEL/C1 survives inside JSON strings while historical malformed-control repair remains outside. Sync/async tests expand the original regression to values and keys across literal/escaped JSON and whole/one-/three-character chunks, with additional context, validation and isolation coverage.

#2899 merged at 18:47:01 UTC that day through `jxnl-oai`, [merge commit 5f352b0](https://github.com/567-labs/instructor/commit/5f352b0085fb2f8adaa26d69a6447ed5cabd2034). Its head `723629d57c05edb996db411e93e7b37ae5c95a8b` is the exact previously source-audited head. The replacement body and final squash commit explicitly reference #2866. Our coauthor trailer exists on the reviewed head but is absent from the final squash commit; final-commit coauthorship is not claimed.

This is the fourth contribution incorporated into a merged maintainer fix, not an eleventh directly merged PR. The source audit is distinct from execution: 101 passing tests are reported by the maintainer and were not rerun during book maintenance. No provider or deployment proof is claimed. It adds neither a new submission nor a merge to the closed 35-submission campaign. Author-directed, AI-assisted work retains human ownership and follow-up responsibility.
