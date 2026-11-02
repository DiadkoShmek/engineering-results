# BlackJAX · стабільні ймовірності Barker MCMC

**Наш [PR #1068](https://github.com/blackjax-devs/blackjax/pull/1068) злитий у main 02.11.2026 о 14:43:52 UTC через `junpenglao`.** Merge commit: `211e1e0cf74d2f87cb7e290d01617c8b9ded4b34`.

## Проблема й рішення

Проміжний `exp(a)` переповнювався під час обчислення `log(1 + exp(a))`. Кінцевий математичний результат міг залишатися скінченним, але sampler отримував неправильну поправку й відхиляв допустимий MCMC-перехід.

У відтворенні з float32 Gaussian target, позицією 20, step size 10 і ключем 2 sampler пропонував приблизно 10.38117 та повертав acceptance 0. Стабільний незалежний розрахунок щільностей давав log acceptance приблизно 46.26094, тобто acceptance 1.

Виправлення використовує `jax.nn.softplus`. Формула Barker зберігається; проміжне переповнення усувається.

## Перевірки

Задокументовані в PR CPU-перевірки:

- 12 нових регресій падають на базі; весь Barker module після зміни — 20 passed.
- NumPy proposal-density oracle: 768 публічних кроків, float32/64, array/PyTree state та constant metrics. 142 розбіжності на базі → 0 на кандидатові; 384 звичайні контролі проходять на обох.
- Окреме рев’ю: 128 додаткових кроків для correlated Gaussian targets, tail values і gradients.
- All-files pre-commit пройшов, включно з Ruff і mypy над 201 source file.

Повний `make test` зупинився на незміненому Makefile. Окреме падіння GIST у CI відтворено на точних base/head: однакові всі 8,000 × 2 sampled positions. GPU/TPU та швидкодію не вимірювали. Position-dependent metric formulas і раніше наявну mixed-dtype поведінку не змінювали.

## English summary

[BlackJAX #1068](https://github.com/blackjax-devs/blackjax/pull/1068) merged into main on 2 November 2026 at 14:43:52 UTC through `junpenglao`.

Barker's direct `log(1 + exp(a))` evaluation could overflow before a finite final result, corrupting proposal probabilities and the acceptance ratio. A valid Gaussian CPU step rejected a proposal for which an independent stable density calculation gives acceptance one. Replacing the helper with `jax.nn.softplus` preserves the formula and avoids that overflow.

Validation documented in the PR: 12 regressions fail on the base; the final Barker module passes 20 tests. A NumPy density oracle checks 768 public float32/64 steps and reduces 142 base mismatches to zero, while preserving 384 ordinary controls. Separate review adds 128 correlated-Gaussian steps and tail-gradient checks. All-files pre-commit passes, including Ruff and mypy.

The full suite was not run: the unchanged Makefile fails to parse. A separate GIST CI failure was reproduced with identical sampled positions on exact base and head. CPU-only proof; no GPU/TPU, speed or position-dependent-metric claim.

[Журнал результатів](../RESULTS.md) · [English results](../RESULTS.en.md) · [Інженерні кейси](../ENGINEERING.md)
