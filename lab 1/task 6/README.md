##  Задание 5 : Пузырьковая сортировка 


**Студент ИТМО,  Нгуен Хыу Жанг  415189**  

## Вариант 16

## Задание

Напишите код на Python и докажите корректность пузырьковой сортировки. Для доказательства корректоности процедуры вам необходимо доказать, что
она завершается и что A′
[1] ≤ A′
[2] ≤ ... ≤ A′
[n], где A′- выход процедуры Bubble_Sort, a n - длина массива A.

Определите время пузырьковой сортировки в наихудшем случае и в среднем
случае и сравните его со временем сортировки вставкой.

Формат входного и выходного файла и ограничения - как в задаче 1.



## Input / Output 

| Input                         |  Output              |
|-------------------------------|----------------------|
| 6<br/>31 41 59 26 41 58       | 26 31 41 41 58 59    |


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