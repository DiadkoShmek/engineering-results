# TensorDict · відтворення й тести для часткових checkpoints

**Результат:** maintainer fix [#3427](https://github.com/pytorch/tensordict/pull/3427) злитий 01.11.2026 й прямо посилається на наш попередній [PR #3426](https://github.com/pytorch/tensordict/pull/3426). Наш PR закритий як superseded, **не merged**.

[English summary](#english-summary) · [Журнал результатів](../RESULTS.md)

## Проблема та наш внесок

Коли `TensorDictParams` був дочірнім `nn.Module`, частковий checkpoint із `strict=False` міг спричиняти помилку замість завантаження наявних ключів і повідомлення про пропущені. Вкладені пропуски, assignment та pre-hooks також потребували окремих перевірок.

Ми дослідили loader, відтворили дефект і запропонували patch із регресіями та differential controls проти native `nn.Module`. У [звіті нашого PR](https://github.com/pytorch/tensordict/pull/3426) зафіксовано 44 failed / 4 passing controls на базі та **251 passed, 2 CUDA skips** у focused suites після нашого виправлення. Ці числа належать нашому кандидату, а не фінальній реалізації мейнтейнера.

## Що прийняв upstream

Мейнтейнер `peterdsharpe` подякував за report і thorough tests та [пояснив вибір меншого рішення](https://github.com/pytorch/tensordict/pull/3426#issuecomment-6563347852): викликати власний `nn.Module._load_from_state_dict` PyTorch замість підтримки його копії в TensorDict. Це зменшує розходження loader при змінах PyTorch.

[PR #3427](https://github.com/pytorch/tensordict/pull/3427) прямо називає DiadkoShmek автором попереднього fix. Його [merge commit](https://github.com/pytorch/tensordict/commit/cd3eeaa6d48bf7674082cbaff64aa2074f2017d5) злитий 01.11.2026 через `peterdsharpe`. Це публічно визнаний внесок у виправлення, реалізоване мейнтейнером; прямого merge нашого patch тут немає.

## English summary

Maintainer [PR #3427](https://github.com/pytorch/tensordict/pull/3427) merged on 1 November 2026 and explicitly credits the earlier fix proposed by DiadkoShmek in [#3426](https://github.com/pytorch/tensordict/pull/3426). Our PR was superseded, not merged.

We contributed defect reproduction, a proposed loader fix, regressions and differential controls against native `nn.Module`. Our candidate's published focused results were 251 passes and two CUDA skips; those numbers do not describe the maintainer's final implementation.

The [closing acknowledgement](https://github.com/pytorch/tensordict/pull/3426#issuecomment-6563347852) thanks the report and thorough tests. `peterdsharpe` chose to delegate to PyTorch's loader rather than maintain a copy. Their [merged implementation](https://github.com/pytorch/tensordict/commit/cd3eeaa6d48bf7674082cbaff64aa2074f2017d5) is the accepted code; our contribution is separately credited.
