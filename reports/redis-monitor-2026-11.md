# Redis Python client

**Наш [PR #4550](https://github.com/redis/redis-py/pull/4550) merged 2026-11-04T15:44:00Z.** Merge commit: `d9fede6eb8c3836a9c632e75303584050f6617de`; merge виконав `petyaslavova`.

## Проблема

Якщо вхід до MONITOR context завершувався помилкою, Python не викликав exit і позичене з’єднання лишалося зайнятим. Пул max_connections=1 міг перестати обслуговувати навіть PING; async setup також має шлях скасування.

## Рішення

Sync/async MONITOR звільняють з’єднання після невдалого входу, від’єднують його від Monitor до exit cleanup та повертають до пулу через finally. Async release захищено shield. Після рев’ю прибрано зайві exception-precedence гілки й варіації, зберігши потрібний maintainer shape.

## Перевірка

Опис PR фіксує перевірку на тимчасовому loopback Redis 8.0.2: 23 passing і 3 native skips для RESP2 та окремо RESP3, включно з ACL denial, повторним використанням одноз’єднаннєвого пулу та async cancellation. GitHub підтверджує прямий merge #4550. Сервер під час оновлення книги не запускався.

Людина визначає напрям, володіє поданням і відповідає за супровід; реалізація та локальна перевірка виконані з AI-допомогою. [Зафіксовані merge-дані](../evidence/redis-monitor-2026-11-04.json).

## English summary

Our [PR #4550](https://github.com/redis/redis-py/pull/4550) merged at 2026-11-04T15:44:00Z, commit `d9fede6eb8c3836a9c632e75303584050f6617de`.

When MONITOR context entry failed, Python did not call exit and the borrowed connection remained checked out. A max_connections=1 pool could stop serving even PING; async setup also has a cancellation path.

Sync/async MONITOR clean up failed entry, detach the connection before exit cleanup and return it to the pool in finally. Async release remains shielded. Review follow-up removed extra exception-precedence branches and permutations while retaining the requested maintainer shape.

The PR records a temporary loopback Redis 8.0.2 run: 23 passing tests and three native skips for each of RESP2 and RESP3, including ACL denial, single-connection pool reuse and async cancellation. GitHub confirms the direct merge of #4550. The server was not restarted for this journal update.

The human directs the work, owns the submission and takes responsibility for follow-up. Implementation and local validation used AI assistance. Focused MONITOR lifecycle change; no full replica/sentinel/cluster/Stack/TLS/Enterprise validation claim. Prior local tests are reported separately from the newly verified upstream merge.

[Журнал](../RESULTS.md) · [English](../RESULTS.en.md) · [Усі PR](../PR_STATUS.md)
