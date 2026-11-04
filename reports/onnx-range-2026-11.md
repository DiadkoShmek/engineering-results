# ONNX Range — точна довжина цілочисельної послідовності

**Наш [PR #8734](https://github.com/onnx/onnx/pull/8734) злитий 04.11.2026 о 01:09:20 UTC.** Merge commit: `22ac1f97bb91b8b3933ed2245fe3151a4979f13c`; злиття виконав `cyyever`. Це пряме злиття нашого PR.

## Проблема

Integer Range shape inference віднімав `start` від `limit` у знаковому типі до перетворення на floating point. Для INT32 з `start = -2147483648`, `limit = 2147483647` і `step = 2147483647` послідовність має три елементи, але знакова різниця переповнювалася, і виведена довжина ставала нульовою. Навіть без такого переповнення floating-point ділення може округлити частку INT64 нижче межі, потрібної для округлення вгору.

## Рішення

Спільний helper для обох історичних схем Range обчислює відстань і модуль кроку як беззнакові величини, а потім виконує точне цілочисельне ділення з округленням угору. Це охоплює обидва напрями та мінімальний від’ємний крок без знакового переповнення. Floating-point шлях не змінено.

## Доказ і межа

[Публічний PR](https://github.com/onnx/onnx/pull/8734) містить приклад і опис рішення; [зафіксовані merge-дані](../evidence/onnx-range-2026-11-04.json) відокремлені від тверджень про тести. Код реалізовано за допомогою Codex. GitHub окремо зафіксував upstream APPROVED від `cyyever` та `justinchuby`. Під час оновлення книги runtime-тести ONNX не запускали повторно. Production-використання не встановлено.

## English summary

Our [PR #8734](https://github.com/onnx/onnx/pull/8734) merged on 4 November 2026 at 01:09:20 UTC, commit `22ac1f97bb91b8b3933ed2245fe3151a4979f13c`, merged by `cyyever`.

Integer Range shape inference previously subtracted in the signed input type before conversion to floating point. The INT32 range from `-2147483648` to `2147483647` with step `2147483647` has three elements, but signed overflow produced an inferred length of zero. Floating-point division can also round an INT64 quotient across a ceiling boundary.

The shared helper for both historical Range schemas uses unsigned distance and step magnitude followed by exact integer ceiling division. It handles both directions and the minimum negative step without signed overflow; the floating-point path remains unchanged.

The PR describes the example and fix; the [merge evidence](../evidence/onnx-range-2026-11-04.json) records acceptance separately from test claims. Codex assisted implementation. GitHub separately records upstream APPROVED reviews from `cyyever` and `justinchuby`. ONNX runtime tests were not rerun for this book refresh, and production use is not established.

[Журнал](../RESULTS.md) · [English results](../RESULTS.en.md) · [Усі PR](../PR_STATUS.md)
