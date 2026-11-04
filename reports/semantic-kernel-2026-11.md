# Microsoft Semantic Kernel

**Наш [PR #14701](https://github.com/microsoft/semantic-kernel/pull/14701) merged 2026-11-04T14:46:53Z.** Merge commit: `78f612433829a9bd858e92521c1249d79865bb4f`; merge виконав `eavanvalkenburg`.

## Проблема

Після раннього закриття або скасування streaming invocation вихідний sync/async Python generator лишався призупиненим. Його finally не звільняв ресурси в момент завершення виклику; утриманий reference робив це незалежним від garbage collection.

## Рішення

Внесок обгортає реальні native generators у closing/aclosing та закриває створений function-invocation stream у Kernel.invoke_stream. Звичайні значення й custom close-bearing результати не отримують чужого cleanup; публічні сигнатури збережено.

## Перевірка

Публічний PR документує 8 failing і 148 passing тестів на базі та 156 passing на кандидатові, 18 доданих сценаріїв із утриманими генераторами й окремі перевірки скасування. GitHub підтверджує прямий merge #14701. Під час оновлення книги runtime-тести не повторювалися.

Людина визначає напрям, володіє поданням і відповідає за супровід; реалізація та локальна перевірка виконані з AI-допомогою. [Зафіксовані merge-дані](../evidence/semantic-kernel-2026-11-04.json).

## English summary

Our [PR #14701](https://github.com/microsoft/semantic-kernel/pull/14701) merged at 2026-11-04T14:46:53Z, commit `78f612433829a9bd858e92521c1249d79865bb4f`.

After early closure or cancellation of a streaming invocation, the underlying sync/async Python generator remained suspended. Its finally block did not release resources when the invocation ended; retaining the generator makes this independent of garbage collection.

The contribution wraps actual native generators in closing/aclosing and closes the owned function-invocation stream in Kernel.invoke_stream. Ordinary values and custom close-bearing results retain their existing behavior; public signatures are unchanged.

The public PR records eight failing and 148 passing baseline tests versus 156 passing candidate tests, 18 added retained-generator scenarios and separate cancellation checks. GitHub confirms the direct merge of #14701. Runtime tests were not repeated for this journal update.

The human directs the work, owns the submission and takes responsibility for follow-up. Implementation and local validation used AI assistance. Native-generator invocation cleanup only; separate prompt/provider forwarding layers and full SDK integration matrix are not established. Merge metadata refreshed; runtime tests not rerun.

[Журнал](../RESULTS.md) · [English](../RESULTS.en.md) · [Усі PR](../PR_STATUS.md)
