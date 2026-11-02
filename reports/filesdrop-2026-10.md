# FilesDrop · два прийняті виправлення API

**Результат:** [PR #32](https://github.com/AndreyBegma/FilesDrop/pull/32) злитий 21.10.2026. Внесок DiadkoShmek із Codex — реалізація двох виправлень надійності та регресійні перевірки.

[English summary](#english-summary) · [Журнал результатів](../RESULTS.md)

## Що змінилося

**Очищення файлів.** Невдала спроба видалення з диска раніше могла залишити файл без запису для повторного очищення. Зміна зберігає невдалі видалення для наступного проходу й фіксує успішні окремо. Перевірка на 501 файл із постійною одиничною відмовою виявила й допомогла усунути блокування наступної партії.

**Deadline під час DNS.** URL-upload міг продовжувати очікувати DNS після спрацювання таймера. Сигнал скасування тепер завершує очікування, зберігаючи чинні перевірки адрес і redirect-поведінки.

## Перевірки та межі

Історичний локальний прогін: **12 API suites, 236 tests passed**; TypeScript і перевірки змінених файлів пройшли. Шість нових регресійних сценаріїв не проходили на початковому коді з тими самими залежностями.

Тести використовували тимчасові файли, in-memory repository та підставні DNS/HTTP-відповіді. Це не production-перевірка. Скасування обмежує очікування запиту, але не скасовує системний DNS lookup. Повністю невдала партія очищення все ще завершується помилкою. [Першоджерело з описом і межами](https://github.com/AndreyBegma/FilesDrop/pull/32).

## English summary

[PR #32](https://github.com/AndreyBegma/FilesDrop/pull/32), merged on 21 October 2026, contains two AI-assisted API fixes: retain failed file removals for retry while committing successful cleanup, and honor the URL-upload deadline while DNS is pending.

The saved local API run passed 236 tests across 12 suites. Six new regression cases failed against the unchanged base. A 501-file counterexample caught batch starvation in the initial candidate and informed the final patch. Tests used disposable files and DNS/HTTP doubles; no production data or live service was tested. Cancellation ends request waiting without cancelling the native OS lookup.
