# Лабораторная работа №2: Сортировка слиянием. Метод декомпозиции.

**Студент ИТМО,  Нгуен Хыу Жанг  415189**  

## Вариант 16

### Навигация

- [ ] [Задача 1 - Сортировка слиянием](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%201/README.md)
- [ ] [Задача 2 - Сортировка слиянием+](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%202/README.md)
- [ ] [Задача 3 - Число инверсий](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%203/READEME.md)
- [ ] [Задача 4 - Бинарный поиск](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%204/README.md)
- [ ] [Задача 5 - Представитель большинства](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%205/README.md)
- [ ] [Задача 6 - Поиск максимальной прибыли](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%206/README.md)
- [ ] [Задача 7 - Поиск максимального подмассива за линейное время](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%207/README.md)
- [ ] [Задача 8 - Умножение многочленов](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%208/README.md)
- [ ] [Задача 9 - Метод Штрассена для умножения матриц](https://github.com/haha523/algorithms-and-data-structures/blob/0d2d7f0c5a4fe5e9e448645f0e82ca7ef21a61c4/lab%202/task%209/README.md)


## Описание
В этой лабораторной работе студенты ознакомятся с сортировкой слиянием и методом декомпозиции. 
Основные задачи включают изучение сортировки слиянием и метода "Разделяй и влавствуй",
их реализация и практика в применении для решения варианта, и при желании 3 дополнительных заданий по выбору, 
написание тестов к ним, создание директории лабораторной согласно требуемой структуре, написание документации 
к каждой задаче, а также одной единой для всей лабораторной.

## Запуск проекта

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/haha523/algorithms-and-data-structures.git
   ```
2. **Перейдите в папку с проектом**
   ```bash
   cd "algorithms-and-data-structures/lab 2"
   ```
3. **Запустить все лабораторные**
    ```bash
    for script in lab*/src/*.py; do PYTHONPATH=$(pwd) python "$script"; done
   ```
4. **Запустить все тесты**
   ```bash
   for script in lab*/tests/*.py; do PYTHONPATH=$(pwd) python "$script"; done
   ```
