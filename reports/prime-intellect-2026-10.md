# Prime Intellect · внесок у виправлення ізоляції агентів

**Результат:** мейнтейнер підтвердив, що наше дослідження й відтворення помилки допомогли сформувати виправлення. Його реалізація злита у Verifiers та prime-rl 24.10.2026. Наш PR був superseded, не merged.

[English summary](#english-summary) · [Журнал результатів](../RESULTS.md)

## Проблема

Налаштування основного навчального запуску потрапляли до окремого агента-судді на зовнішньому клієнті. Параметри конкретного inference-сервера могли спричиняти HTTP 400 у іншого провайдера.

Початкову [задачу #2923](https://github.com/PrimeIntellect-ai/verifiers/issues/2923) відкрив `rasdani`. Внесок DiadkoShmek із Codex — дослідження шляху конфігурації, перевірне відтворення, матриця сценаріїв і запропонований [patch #2925](https://github.com/PrimeIntellect-ai/verifiers/pull/2925).

## Від внеску до прийнятого виправлення

| Дата | Подія | Доказ |
|---|---|---|
| 20.10.2026 | Відкрито наш PR з відтворенням і перевірками | [#2925](https://github.com/PrimeIntellect-ai/verifiers/pull/2925) |
| 24.10.2026 | Мейнтейнер підтвердив вплив дослідження на рішення | [Коментар](https://github.com/PrimeIntellect-ai/verifiers/pull/2925#issuecomment-6385135636) |
| 24.10.2026 | Злито варіант мейнтейнера у Verifiers | [#2973](https://github.com/PrimeIntellect-ai/verifiers/pull/2973) |
| 24.10.2026 | Злито пов'язану зміну у prime-rl | [#4243](https://github.com/PrimeIntellect-ai/prime-rl/pull/4243) |

Мейнтейнер написав:

> Thanks for the clear repro and the investigation. They shaped the fix.

Він також назвав наш приклад із суддею перевіркою для виправлення. [Першоджерело](https://github.com/PrimeIntellect-ai/verifiers/pull/2925#issuecomment-6385135636).

## Архітектурний вибір

Наш варіант припиняв успадкування загальних sampling-параметрів, коли агент явно задавав модель або клієнта. Мейнтейнер обрав межу **клієнта**: окрема модель або LoRA на тому самому сервері зберігає спільні параметри; окремий клієнт отримує власні.

Це відмінність контрактів. До основної гілки внесено його реалізацію; наш внесок у дослідження публічно визнано. [Рішення й міграційні умови](https://github.com/PrimeIntellect-ai/verifiers/pull/2973).

<details>
<summary>Методика, дані та обмеження</summary>

- Початкова база нашої зміни: `512b8f77f14de2a7323bd4f497610d029a8bf148`.
- Власна матриця запропонованого контракту: 11 failed / 7 passed до зміни; 18 passed після. Це 18 сценаріїв, а не 11 окремих продуктових дефектів.
- Історичний локальний unit-прогін: 189 passed, 1 skipped через відсутню необов'язкову Harbor dependency. Перевірки стилю й типів пройшли.
- Матриця охоплювала окремі model/client overrides, явні значення, очищення параметрів, незмінність входів і повторне розв'язання конфігурації.
- Живі provider-запити й навчальний запуск нашою перевіркою не виконувалися.
- Ці числа описують збережений прогін 20 жовтня, не новий benchmark сьогодні.

</details>

## English summary

**Outcome:** the Verifiers maintainer explicitly acknowledged that our reproduction and investigation shaped the fix. Their implementation merged in [Verifiers #2973](https://github.com/PrimeIntellect-ai/verifiers/pull/2973) and [prime-rl #4243](https://github.com/PrimeIntellect-ai/prime-rl/pull/4243) on 24 October 2026.

Another contributor filed the [original issue](https://github.com/PrimeIntellect-ai/verifiers/issues/2923). The AI-assisted contribution was investigation, reproduction, a regression matrix and [proposed patch #2925](https://github.com/PrimeIntellect-ai/verifiers/pull/2925). That PR was superseded, not merged. The maintainer chose client-scoped inheritance so model-only overrides on the same client retain policy sampling.

The saved local matrix moved from 11 failing / 7 passing scenarios to 18 passing; the unit suite had 189 passes and one optional-dependency skip. No live inference or training run was performed. These are dated local checks, separate from the [public maintainer acknowledgement](https://github.com/PrimeIntellect-ai/verifiers/pull/2925#issuecomment-6385135636).
