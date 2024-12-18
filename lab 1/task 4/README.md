##  Задание 3 : Линейный поиск 


**Студент ИТМО,  Нгуен Хыу Жанг  415189**  

## Вариант 16

## Задание

Рассмотрим задачу поиска.

- Формат входногофайла. Последовательность изnчиселA = a1, a2, . . . , an
в первой строке, числа разделены пробелом, и значение V во второй строке.
Ограничения: 0 ≤ n ≤ 10^3, −10^3 ≤ ai, V ≤ 10^3

- Формат выходного файла. Одно число - индекс i, такой, что V = A[i], или значение −1, если V в отсутствует.

- Напишите код линейного поиска, при работе которого выполняется сканирование последовательности в поисках значения V .

- Если число встречается несколько раз, то выведите, сколько раз встречается число и все индексы i через запятую.

- Дополнительно: попробуйте найти свинью, как в лекции. Используйте во входном файле последовательность слов из лекции, и найдите соответствующий индекс.


## Input / Output 

| Input                         |  Output    |
|-------------------------------|------------|
| 1 2 3 4 2 5<br/>2             | 2: 1, 4    |


## Ограничения по времени и памяти

- Ограничение по времени. 2 сек.
- Ограничение по памяти. 256 мб.

## Запуск проекта
1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/haha523/algorithms-and-data-structures.git
   ```
2. **Перейдите в папку с проектом**
   ```bash
   cd "algorithms-and-data-structures/lab 1"
   ```
3. **Запустить все лабораторные**
    ```bash
   python src/main.py
   ```
4. **Запустить все тесты**
    ```bash
   python -documents_count unittest discover -v
   ```
