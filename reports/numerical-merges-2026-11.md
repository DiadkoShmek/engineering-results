# torchode, Lineax і NumPyro

Три внески, злиті з 6 по 9 листопада 2026 року. Напрям, подання та супровід — авторські. Дослідження, код і перевірки виконано з AI-інструментами.

## torchode · backsolve adjoint

[PR #56](https://github.com/martenlienen/torchode/pull/56) · 2026-11-06T10:56:19Z · [40894a2](https://github.com/martenlienen/torchode/commit/40894a21a9f7a51133f79ea2bbdb4bccd5a29162) · злив `martenlienen`.

Backsolve adjoint зупинявся на першій точці спостереження. Якщо вона лежала після початкового часу вздовж інтегрування, градієнт втрачав внесок початкового інтервалу. Додали зворотне інтегрування від першої точки до початкового часу. Для елементів батчу, які вже на початковому часі, збережено їхній стан.

Власник підтвердив, що фікс увійшов у [torchode 1.1.0](https://pypi.org/project/torchode/1.1.0/). [Коментар про реліз](https://github.com/martenlienen/torchode/pull/56#issuecomment-6721646009).

Злиття і реліз підтверджено. Локальні прогони описані в PR і датовані роботою над виправленням.

## Lineax · reshaping identities

[PR #268](https://github.com/patrick-kidger/lineax/pull/268) · 2026-11-09T21:40:44Z · [316b691](https://github.com/patrick-kidger/lineax/commit/316b6913025f451e5d5518d4ff09d156d99a5634) · злив `jpbrodrick89`.

Матеріалізація композиції могла викинути тотожний оператор, що змінює структуру PyTree, хоча кількість елементів збігається. Скорочуємо тотожний оператор лише зі збіжними вхідною й вихідною структурами. Те саме обмеження діє для згортання до структурованої форми.

Рев’юер описав крайові випадки для окремого продовження. [Коментар](https://github.com/patrick-kidger/lineax/pull/268#issuecomment-6705754172).

Прямий merge для описаного класу композицій. Подальші випадки матеріалізації залишаються предметом окремого виправлення.

## NumPyro · GaussianStateSpace variance

[PR #2405](https://github.com/pyro-ppl/numpyro/pull/2405) · 2026-11-09T10:13:37Z · [be7c78f](https://github.com/pyro-ppl/numpyro/commit/be7c78f254713f6cb7612d064604cd911f1efe80) · злив `juanitorduz`.

Відновлення осі часу через swapaxes переставляло батч-осі дисперсії. Для прямокутного батчу це могло викликати помилку broadcasting. Перенесли вісь часу через moveaxis зі збереженням порядку решти осей. Додали батч (2, 3) із нетривіальною матрицею переходу до наявного набору тестів.

Прямий merge виправлення дисперсії. Зміни параметричних батчів RecursiveLinearTransform обговорюються окремо.

## English summary

**[torchode · backsolve adjoint](https://github.com/martenlienen/torchode/pull/56)**. The backsolve adjoint stopped at the first evaluation and omitted the interval to the initial time when it lay earlier along the integration path. Integrate back from the first evaluation to the initial time and preserve the augmented state for already-aligned batch members. PR #56 merged. The PR documents an analytic example and six regression cases. The owner confirmed inclusion in 1.1.0, published on PyPI.

**[Lineax · reshaping identities](https://github.com/patrick-kidger/lineax/pull/268)**. Materializing a composition could erase an identity that reshaped the PyTree despite preserving the number of elements. Only eliminate identities with matching input and output structures. Require structure compatibility before folding to a structured operator. PR #268 merged. The reviewer identified further edge cases for a separate follow-up.

**[NumPyro · GaussianStateSpace variance](https://github.com/pyro-ppl/numpyro/pull/2405)**. Using swapaxes to restore the variance time axis reordered batch axes and could trigger a broadcast error on a nonsquare batch. Move only the time axis. Add a (2, 3) batch with a dense transition to the existing variance and Monte Carlo tests. PR #2405 merged into master. The regression runs through the existing distribution tests.
