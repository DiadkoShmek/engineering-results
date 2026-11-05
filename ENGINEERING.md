# Інженерні кейси

AI-assisted engineering: проблема, рішення, перевірка та зовнішній наслідок.

## Прийняті виправлення

- **[ONNX IR #533](reports/onnx-ir-dropout-2026-11.md):** CSE зберігає незалежні Dropout evaluations; merged 05.11.2026.

- **[ONNX IR #529](reports/onnx-ir-iterator-2026-11.md):** finite iterator заміни graph I/O slices зберігають declarations і ownership; merged 05.11.2026.

- **[OTT-JAX](reports/ott-2026-11.md):** custom implicit-differentiation solver дістає керування; #716 merged 05.11.2026 після maintainer pruning тесту та 9 hosted SUCCESS checks.

- **[PyLops](reports/pylops-2026-11.md):** орієнтація dense nonstationary convolution узгоджена з forward/adjoint дією оператора; наш #837 merged 04.11.2026.

- **[Microsoft Semantic Kernel](reports/semantic-kernel-2026-11.md):** завершення sync/async native generators після закриття streaming invocation; #14701 merged 04.11.2026.
- **[Redis Python client](reports/redis-monitor-2026-11.md):** повернення MONITOR connection до пулу після невдалого context entry; #4550 merged 04.11.2026.

- **[ONNX Range](reports/onnx-range-2026-11.md):** точна довжина integer Range без переповнення знакової різниці; наш #8734 merged 04.11.2026.

- **[ONNX IR](reports/onnx-ir-2026-11.md):** збереження публічних output names і ownership під час усунення Identity; наш #521 merged 03.11.2026.

- **[TensorLy](reports/tensorly-2026-11.md):** weights і mask для single-factor Khatri-Rao; компактна регресія після рев’ю. Наш #695 merged.

- **[BlackJAX](reports/blackjax-2026-11.md):** стабільні proposal probabilities у Barker MCMC; NumPy density oracle й CPU JIT-перевірки. Наш #1068 merged.

- **[Braintrust](reports/braintrust-2026-11.md):** streaming UTF-8 decoder; регресії всіх byte boundaries. Наш #2701 merged.
- **[Kraft](reports/kraft-2026-11.md):** повторний init оновлює skills при наявній MCP-реєстрації. Наш #1227 merged.
- **[FilesDrop](reports/filesdrop-2026-10.md):** повтор cleanup після відмови та deadline під час DNS. Наш #32 merged.

## Дослідження у виправленнях мейнтейнерів

- **[Instructor](reports/instructor-2026-11.md):** Unicode streaming finding і regressions увійшли в консолідацію #2899; наш #2866 superseded. Final squash посилається на #2866, але не зберіг head coauthor trailer.

- **[Prime Intellect](reports/prime-intellect-2026-10.md):** відтворення сформувало виправлення ізоляції агентів у Verifiers і prime-rl. Наш patch superseded.
- **[TensorDict](reports/tensordict-2026-11.md):** partial checkpoints, differential controls і тести; мейнтейнер обрав менший fix через власний loader PyTorch. Наш #3426 superseded; #3427 merged із credit.

- **[Apache TVM-FFI](reports/tvm-ffi-2026-11.md):** structural-hash finding; мейнтейнер замінив #897 constructor-level #898, який злитий; наш #897 superseded.

## M7 MCP · аудит

[Review/triage credit у v3.18.1, оригінальний PDF і focused follow-up](reports/m7-2026-10.md). Незакриті сценарії збережені.

## Змагання

- **[CodinGame · Mad Pod Racing](reports/codingame-2026-10.md):** відхилена гіпотеза після 2/8; умовний результат 221/400; зовнішня арена окремо.
- **Zoria / UA SKILLS:** призер сезону. [Оголошення та історія](RESULTS.md#zoria-2026--підсумок-ua-skills); інженерний розбір ще не опублікований.

## Вибрані сигнали рев’ю · 05.11.2026, 19:10 UTC

- **[Triton #12611](reports/triton-2026-11.md):** OPEN; upstream merge не підтверджено.
- **[Docling Core #953](https://github.com/docling-project/docling-core/pull/953):** OPEN, aggregate REVIEW_REQUIRED. Поточні CI та всі правила merge цим зрізом не засвідчуються.
- **[OTT #716](https://github.com/ott-jax/ott/pull/716):** мейнтейнер michalk8 оновив гілку та скоротив тест; Lint/Tests на head 60222b1 чекають дозволу запуску (ACTION_REQUIRED), merge немає.
- **[ONNX IR #533](https://github.com/onnx/ir-py/pull/533#discussion_r4484767254):** justinchuby схвалив із питанням щодо зміни тесту та flakiness; OPEN, aggregate reviewDecision лишається null.
- **[ONNX IR #531](https://github.com/onnx/ir-py/pull/531#pullrequestreview-5790485437):** CHANGES_REQUESTED щодо практичної потреби розрізняти signed zero; потрібна предметна відповідь, merge немає.

[Повний датований стан PR](PR_STATUS.md) · [English](PR_STATUS.en.md). Це вибрані сигнали, не повний аудит CI/threads. Схвалення та локальні тести не є merge.

## Як читати

Ігровий бот приймає рішення в матчі. AI-агент розробки досліджує, пише код і тестує. Людина визначає напрям, володіє поданням, погоджує зовнішні дії й відповідає за супровід.

Це не контрольований порівняльний бенчмарк AI-моделей. Час, вартість і людські втручання не виміряні зіставно. Власний merged patch, credited investigation та аудит — різні результати.

[Журнал](RESULTS.md) · [English results](RESULTS.en.md) · [Профіль](https://github.com/DiadkoShmek)

## Подані виправлення · 04.11.2026 UTC

[Лезо — 20 нових PR у 18 репозиторіях](reports/lezo-2026-11.md): компіляція, автоматичне диференціювання, тензорні операції, ймовірнісні моделі та лінійні оператори. [English summary](reports/lezo-2026-11.md#english-summary). Статус кожного PR і перевірений source commit наведено у звіті.

[Новий прохід «Лезо»: завершено 35 подань](reports/lezo50-2026-11.md). Подання й нові merge попередніх PR обліковані окремо.
