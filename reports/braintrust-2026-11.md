# Braintrust SDK · UTF-8 у потоковому логуванні

**Результат:** наш [PR #2701](https://github.com/braintrustdata/braintrust-sdk-javascript/pull/2701) злитий 02.11.2026; merger — `lforst`.

[English summary](#english-summary) · [Журнал результатів](../RESULTS.md)

## Проблема та зміна

Коли байти одного UTF-8 символу потрапляли в різні chunks `ReadableStream<Uint8Array>`, окреме декодування кожного chunk псувало текст у записі `/logs3`. Звичайний ASCII та той самий Unicode в одному chunk проходили.

Зберегли стан `TextDecoder` між байтовими chunks, використали декодований текст для передачі й накопичення та завершили декодування на EOF або перед небайтовим chunk. Порядок string/structured chunks і потік, який читає застосунок, збережені.

## Перевірка та прийняття

За [опублікованим PR-звітом](https://github.com/braintrustdata/braintrust-sdk-javascript/pull/2701), початковий код із фінальними focused tests мав **6 failed / 13 passed**; пов'язані logger/stream suites після виправлення — **178 passed** на Node 24.14 та 26.8.2. Перевірки включали всі розрізи дво-, три- й чотирибайтових символів, змішані chunks, незавершений EOF та помилки.

Додатковий незалежний прогін охопив 1 051 byte-boundary/error/cancellation/isolation checks. Це історичні локальні результати з підставною HTTP-межею, а не новий прогін цієї сторінки. Browser runtime, весь monorepo і real-provider e2e не перевірялися.

[Merge commit](https://github.com/braintrustdata/braintrust-sdk-javascript/commit/27181871510a46d294b7fc96d1d76496443a8a20) підтверджує прийняття коду upstream; впровадження в клієнтів тут не заявляю.

## English summary

Our [PR #2701](https://github.com/braintrustdata/braintrust-sdk-javascript/pull/2701) merged on 2 November 2026 through `lforst`. It fixes corrupted logged Unicode when a UTF-8 character crosses raw byte-stream chunk boundaries: retain streaming `TextDecoder` state and flush it at EOF or before non-byte chunks.

The published regression moved from 6 failures / 13 passing controls to passing; related logger/stream suites passed 178 tests on Node 24.14 and 26.8.2. An independent run added 1,051 boundary/error/cancellation/isolation checks. These dated local checks used an HTTP test boundary; they do not cover the full monorepo, browsers or real providers. The [merge commit](https://github.com/braintrustdata/braintrust-sdk-javascript/commit/27181871510a46d294b7fc96d1d76496443a8a20) establishes upstream acceptance.
