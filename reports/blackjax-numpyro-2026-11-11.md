# BlackJAX і NumPyro · три виправлення

Три власні PR злиті 11 листопада 2026 року. Подання та супровід авторські. Дослідження й реалізація виконані з AI-інструментами.

## NumPyro · маски Cat

Компоненти Cat з різним рангом подій могли повертати маски неправильної форми, тож перевірений log_prob падав на допустимих значеннях. Звели перевірки до спільного рангу. Частини батчу конкатенуються, а перевірки частин однієї події поєднуються логічним AND.

П’ять регресій у таблиці обмежень і одна наскрізна перевірка log_prob відтворюють дефект. Власний PR #2404 злитий після двох схвалень.

[PR #2404](https://github.com/pyro-ppl/numpyro/pull/2404) · [Коміт злиття](https://github.com/pyro-ppl/numpyro/commit/c347fbe3bf6f0d45dff337d8c98a0c6fe63a0101)

## BlackJAX · вісь вибірок Schrödinger–Föllmer

Оцінка дрейфу могла згортати вісь параметрів замість осі Монте-Карло. Матричний параметр міг дати інший дрейф за ту саму плоску модель. Середнє береться явно за першою віссю вибірок. Регресії звіряють один крок і траєкторії в початкових та плоских координатах.

Власний PR #1071 схвалений і злитий. Публічний опис містить незалежний числовий еталон і датований CPU-прогін.

[PR #1071](https://github.com/blackjax-devs/blackjax/pull/1071) · [Коміт злиття](https://github.com/blackjax-devs/blackjax/commit/1d68458a521197fa8117f2bb85bad22e1f2372cd)

## BlackJAX · ціль мутації SMC

У partial-posterior SMC мутація брала нову ціль до застосування відношення щільностей. На точному гаусовому прикладі це двічі враховувало нові дані. Мутація зберігає попередній апостеріорний розподіл. Новий внесок надходить через наступне оновлення ваг.

Власний PR #1072 схвалений і злитий. Публічний тест зі штатним HMC звіряє частинки, ваги й приріст нормалізатора.

[PR #1072](https://github.com/blackjax-devs/blackjax/pull/1072) · [Коміт злиття](https://github.com/blackjax-devs/blackjax/commit/e8db80fa586a12fdca044fbdfd3f364fdeb58619)

## English summary

**[NumPyro · Cat event masks](https://github.com/pyro-ppl/numpyro/pull/2404)**. Mixed event ranks in Cat could produce invalid mask shapes and prevent validated log_prob on valid values. Reduce component checks to the common event rank. Concatenate batch slices and AND the checks for slices of one event. Five constraint rows and one end-to-end validated log_prob regression reproduce the bug. PR #2404 merged after two approvals.

**[BlackJAX · Schrödinger–Föllmer sample axis](https://github.com/blackjax-devs/blackjax/pull/1071)**. The drift estimator could contract a parameter axis instead of the Monte Carlo axis. A matrix parameter could yield a different drift from equivalent flat coordinates. Reduce explicitly over the leading sample axis. Compare single steps and trajectories against equivalent flattened coordinates. PR #1071 was approved and merged. Its description records an independent numerical reference and dated CPU tests.

**[BlackJAX · SMC mutation target](https://github.com/blackjax-devs/blackjax/pull/1072)**. Partial-posterior SMC mutated toward the new target before applying the density ratio. An exact Gaussian example double-counted new data. Preserve the previous posterior during mutation and account for new data in the subsequent weight update. PR #1072 was approved and merged. A stock HMC regression checks particles, weights and normalizer increments.
