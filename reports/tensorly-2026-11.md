# TensorLy - ваги й маски для одного множника Khatri-Rao

**Наш [PR #695](https://github.com/tensorly/tensorly/pull/695) злитий у main 02.11.2026 о 23:54:45 UTC через `JeanKossaifi`.** Merge commit: `cdde62fa67b2a7424ed292223de3a049967733fe`. Стан перевірено 03.11.2026 UTC. Це пряме злиття нашого PR.

## Проблема й рішення

Коли після `skip_matrix` або від початку лишався один множник, `khatri_rao` повертав матрицю до застосування необов’язкових ваг стовпців та маски рядків. Операція мовчки давала неправильний результат; такий шлях використовується й у зважених matrix-CP градієнтах.

Виправлення застосовує `weights` і `mask` у single-factor шляху обох реалізацій `core_tenalg` та `einsum_tenalg`. Звичайний результат без цих опцій і multi-factor шляхи збережені.

Для матриці `[[1,2,3],[4,5,6]]`, ваг `[2,0,-1]` і маски `[0,2]` правильний результат - `[[0,0,0],[16,0,-12]]`.

## Рев’ю і перевірки

[JeanKossaifi попросив залишити один коротший тест](https://github.com/tensorly/tensorly/pull/695#issuecomment-6588215230). Додані 18 варіантів зведено до одного компактного тесту з буквальними expected values; production-код при цьому не змінювався. [Відповідь із виконаною зміною](https://github.com/tensorly/tensorly/pull/695#issuecomment-6588570359) передувала [підтвердженню merge](https://github.com/tensorly/tensorly/pull/695#issuecomment-6591551013).

Перевірки, виконані перед поданням останньої версії:

- Exact-base RED у всіх чотирьох режимах NumPy/PyTorch та core/einsum.
- Окремі мутанти без weights або без mask теж відхиляються цим тестом.
- Два відповідні test modules: по 70 PASS у кожному з чотирьох режимів на CPU.
- Black перевірив усі 156 source/test файлів; diff check пройшов.

Повний репозиторій, документацію, GPU та решту backend/version matrix не запускали. Попередню велику oracle-кампанію після скорочення тестів не повторювали. Під час фіксації зовнішнього результату runtime-тести заново не запускали; злиття звірено за нативними даними GitHub.

## English summary

Our [PR #695](https://github.com/tensorly/tensorly/pull/695) merged into main on 2 November 2026 at 23:54:45 UTC through `JeanKossaifi`, merge commit `cdde62fa67b2a7424ed292223de3a049967733fe`. The disposition was verified on 3 November UTC. This is a direct merge of our PR.

A single-factor Khatri-Rao product returned before applying column weights and a row mask, including the case left after `skip_matrix`. Both tenalg implementations now apply the optional factors before returning. For `[[1,2,3],[4,5,6]]`, weights `[2,0,-1]` and mask `[0,2]`, the expected result is `[[0,0,0],[16,0,-12]]`.

Following maintainer review, the added tests were reduced from 18 variants to one compact regression with literal expected values; the implementation was unchanged by that revision. The regression fails on the exact base in all four NumPy/PyTorch and core/einsum modes and rejects independently dropping either multiplier. The two relevant modules passed 70 tests per mode on CPU; Black checked all 156 source/test files.

The full repository, documentation, GPU and remaining backend/version matrix were not run. The earlier large oracle campaign was not repeated for the test-only revision. No runtime tests were repeated to record the merge; GitHub merge metadata and the maintainer’s acknowledgement provide the external evidence.

[Журнал результатів](../RESULTS.md) · [English results](../RESULTS.en.md) · [Інженерні кейси](../ENGINEERING.md)
