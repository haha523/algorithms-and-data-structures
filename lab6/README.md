# Лабораторная работа №6: Хеширование. Хеш-таблицы.

**Студент ИТМО,  Нгуен Хыу Жанг  415189**  

## Вариант 16

### Навигация

- [ ] [Задача 1 - Множество](https://github.com/haha523/algorithms-and-data-structures/blob/fe3c7c3bc62e468e2e451dc52847b593dcfb2196/lab6/task%201/README.md)
- [ ] [Задача 2 - Телефонная книга](https://github.com/haha523/algorithms-and-data-structures/blob/fe3c7c3bc62e468e2e451dc52847b593dcfb2196/lab6/task%202/README.md)
- [ ] [Задача 3 - Хеширование с цепочками](https://github.com/haha523/algorithms-and-data-structures/blob/fe3c7c3bc62e468e2e451dc52847b593dcfb2196/lab6/task%203/README.md)
- [ ] [Задача 4 - Прошитый ассоциативный массив](https://github.com/haha523/algorithms-and-data-structures/blob/fe3c7c3bc62e468e2e451dc52847b593dcfb2196/lab6/task%204/README.md)
- [ ] [Задача 5 - Выборы в США](https://github.com/haha523/algorithms-and-data-structures/blob/fe3c7c3bc62e468e2e451dc52847b593dcfb2196/lab6/task%205/README.md)
- [ ] [Задача 6 - Фибоначчи возвращается](https://github.com/haha523/algorithms-and-data-structures/blob/fe3c7c3bc62e468e2e451dc52847b593dcfb2196/lab6/task%206/README.md)
- [ ] [Задача 7 - Драгоценные камни](https://github.com/haha523/algorithms-and-data-structures/blob/fe3c7c3bc62e468e2e451dc52847b593dcfb2196/lab6/task%207/README.md)
- [ ] [Задача 8 - Почти интерактивная хеш-таблица](https://github.com/haha523/algorithms-and-data-structures/blob/fe3c7c3bc62e468e2e451dc52847b593dcfb2196/lab6/task%208/README.md)


## Описание

Целью лабораторной работы №6 является ознакомление студентов с такими понятиями, как множество, словари, хеш-таблицы и хеш-функции.

Задачи:

- Базовый уровень: Студенты должны решить 3 задачи, при этом необходимо выполнить два условия:

- Все три задачи не могут стоять подряд (например, набор (1, 2, 3) — нельзя, а (1, 2, 4) — можно).

- Номер одной из задач определяется по хеш-функции: 𝐻(𝑣) = (𝐴 ⋅ 𝑣 mod 𝑝) mod 9, где 𝐴 — последние 2 числа номера группы, 𝑣 — номер в списке группы, 𝑝 — следующее простое число, большее количества студентов в группе.
- Номер второй задачи может быть найден по принципу: H(𝑣) = ((A ⋅ 𝑣 + B) modp ) mod 9, где B — сумма кодов ASCII всех букв фамилии.

- За базовый уровень можно получить максимум 4 балла, что в сумме с работой (0,5 балла) и отчетом (1 балл) составляет 5,5 балла, достаточных для зачета.

- Продвинутый уровень: Студенты должны решить 5 задач или больше, с учётом тех же принципов, что и для базового уровня. Максимально возможная оценка — 7,5 баллов.


## Запуск проекта


1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/haha523/algorithms-and-data-structures.git
   ```
2. **Перейдите в папку с проектом**
   ```bash
   cd "algorithms-and-data-structures/lab6"
   ```
3. **Запустить все лабораторные**
    ```bash
    for script in lab*/src/*.py; do PYTHONPATH=$(pwd) python "$script"; done
   ```
4. **Запустить все тесты**
   ```bash
   for script in lab*/tests/*.py; do PYTHONPATH=$(pwd) python "$script"; done
   ```



