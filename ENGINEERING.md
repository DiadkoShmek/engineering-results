# Інженерні кейси

AI-assisted engineering: проблема, рішення, перевірка та зовнішній наслідок.

## Прийняті виправлення

- **[ONNX IR](reports/onnx-ir-2026-11.md):** збереження публічних output names і ownership під час усунення Identity; наш #521 merged 03.11.2026.

- **[TensorLy](reports/tensorly-2026-11.md):** weights і mask для single-factor Khatri-Rao; компактна регресія після рев’ю. Наш #695 merged.

- **[BlackJAX](reports/blackjax-2026-11.md):** стабільні proposal probabilities у Barker MCMC; NumPy density oracle й CPU JIT-перевірки. Наш #1068 merged.

- **[Braintrust](reports/braintrust-2026-11.md):** streaming UTF-8 decoder; регресії всіх byte boundaries. Наш #2701 merged.
- **[Kraft](reports/kraft-2026-11.md):** повторний init оновлює skills при наявній MCP-реєстрації. Наш #1227 merged.
- **[FilesDrop](reports/filesdrop-2026-10.md):** повтор cleanup після відмови та deadline під час DNS. Наш #32 merged.

## Дослідження у виправленнях мейнтейнерів

- **[Prime Intellect](reports/prime-intellect-2026-10.md):** відтворення сформувало виправлення ізоляції агентів у Verifiers і prime-rl. Наш patch superseded.
- **[TensorDict](reports/tensordict-2026-11.md):** partial checkpoints, differential controls і тести; мейнтейнер обрав менший fix через власний loader PyTorch. Наш #3426 superseded; #3427 merged із credit.

- **[Apache TVM-FFI](reports/tvm-ffi-2026-11.md):** structural-hash finding; мейнтейнер замінив #897 constructor-level #898, який злитий; наш #897 superseded.

## M7 MCP · аудит

[Review/triage credit у v3.18.1, оригінальний PDF і focused follow-up](reports/m7-2026-10.md). Незакриті сценарії збережені.

## Змагання

- **[CodinGame · Mad Pod Racing](reports/codingame-2026-10.md):** відхилена гіпотеза після 2/8; умовний результат 221/400; зовнішня арена окремо.
- **Zoria / UA SKILLS:** призер сезону. [Оголошення та історія](RESULTS.md#zoria-2026--підсумок-ua-skills); інженерний розбір ще не опублікований.

## Review-stage · 03.11.2026 UTC

- **[Triton #12611](reports/triton-2026-11.md):** оцінка вартості CUDA f32 sin/cos під час rematerialization. Поданий, OPEN; до merged-результатів не зарахований.
- **[ONNX #8734](https://github.com/onnx/onnx/pull/8734):** точний integer Range shape inference; APPROVED, але OPEN.
- **[Semantic Kernel #14701](https://github.com/microsoft/semantic-kernel/pull/14701):** cleanup native generators; APPROVED, але OPEN.
- **[Docling Core #953](https://github.com/docling-project/docling-core/pull/953):** references скопійованих comments; Mergify чекає двох approving reviews.

[Повний датований стан PR](PR_STATUS.md) · [English](PR_STATUS.en.md). Схвалення та локальні тести не є merge.

## Як читати

Ігровий бот приймає рішення в матчі. AI-агент розробки досліджує, пише код і тестує. Людина визначає напрям і погоджує зовнішні дії.

Це не контрольований порівняльний бенчмарк AI-моделей. Час, вартість і людські втручання не виміряні зіставно. Власний merged patch, credited investigation та аудит — різні результати.

[Журнал](RESULTS.md) · [English results](RESULTS.en.md) · [Профіль](https://github.com/DiadkoShmek)
