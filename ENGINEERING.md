# Інженерні кейси

AI-assisted engineering: проблема, рішення, перевірка та зовнішній наслідок.

## Прийняті виправлення

- **[BlackJAX](reports/blackjax-2026-11.md):** стабільні proposal probabilities у Barker MCMC; NumPy density oracle й CPU JIT-перевірки. Наш #1068 merged.

- **[Braintrust](reports/braintrust-2026-11.md):** streaming UTF-8 decoder; регресії всіх byte boundaries. Наш #2701 merged.
- **[Kraft](reports/kraft-2026-11.md):** повторний init оновлює skills при наявній MCP-реєстрації. Наш #1227 merged.
- **[FilesDrop](reports/filesdrop-2026-10.md):** повтор cleanup після відмови та deadline під час DNS. Наш #32 merged.

## Дослідження у виправленнях мейнтейнерів

- **[Prime Intellect](reports/prime-intellect-2026-10.md):** відтворення сформувало виправлення ізоляції агентів у Verifiers і prime-rl. Наш patch superseded.
- **[TensorDict](reports/tensordict-2026-11.md):** partial checkpoints, differential controls і тести; мейнтейнер обрав менший fix через власний loader PyTorch. Наш #3426 superseded; #3427 merged із credit.

- **[Apache TVM-FFI](reports/tvm-ffi-2026-11.md):** structural-hash finding; мейнтейнер замінив #897 constructor-level #898, який ще OPEN.

## M7 MCP · аудит

[Review/triage credit у v3.18.1, оригінальний PDF і focused follow-up](reports/m7-2026-10.md). Незакриті сценарії збережені.

## Змагання

- **[CodinGame · Mad Pod Racing](reports/codingame-2026-10.md):** відхилена гіпотеза після 2/8; умовний результат 221/400; зовнішня арена окремо.
- **Zoria / UA SKILLS:** призер сезону. [Оголошення та історія](RESULTS.md#zoria-2026--підсумок-ua-skills); інженерний розбір ще не опублікований.

## Review-stage · 02.11.2026

[Semantic Kernel #14701](https://github.com/microsoft/semantic-kernel/pull/14701): cleanup native generators; `eavanvalkenburg` APPROVED. PR OPEN, не merged; до завершених результатів не зарахований.

## Як читати

Ігровий бот приймає рішення в матчі. AI-агент розробки досліджує, пише код і тестує. Людина визначає напрям і погоджує зовнішні дії.

Це не контрольований порівняльний бенчмарк AI-моделей. Час, вартість і людські втручання не виміряні зіставно. Власний merged patch, credited investigation та аудит — різні результати.

[Журнал](RESULTS.md) · [English results](RESULTS.en.md) · [Профіль](https://github.com/DiadkoShmek)
