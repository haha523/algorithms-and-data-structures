##  Задание 6 : Сортировка целых чисел 


**Студент ИТМО,  Нгуен Хыу Жанг  415189**  

## Вариант 16

## Задание

В этой задаче нужно будет отсортировать много неотрицательных целых чисел.
Вам даны два массива, A и B, содержащие соответственно n и m элементов.
Числа, которые нужно будет отсортировать, имеют вид Ai
· Bj , где 1 ≤ i ≤ n и
1 ≤ j ≤ m. Иными словами, каждый элемент первого массива нужно умножить
на каждый элемент второго массива.
Пусть из этих чисел получится отсортированная последовательность C длиной
n · m. Выведите сумму каждого десятого элемента этой последовательности (то
есть, C1 + C11 + C21 + ...).

- Формат входного файла (input.txt). В первой строке содержатся числа n
и m (1 ≤ n, m ≤ 6000) – размеры массивов. Во второй строке содержится
n чисел – элементы массива A. Аналогично, в третьей строке содержится
m чисел — элементы массива B. Элементы массива неотрицательны и не
превосходят 40000.

- Формат выходного файла (output.txt). Выведите одно число — сумму
каждого десятого элемента последовательности, полученной сортировкой
попарных произведенй элементов массивов A и B.

- Ограничение по времени распространяется на сортировку, без учета
времени на перемножение. Подумайте, какая сортировка будет эффективнее, сравните на практике.

- Однако бытует мнение на OpenEdu, неделя 3, задача 2, что эту задачу
можно решить на Python и уложиться в 2 секунды, включая в общее время
перемножение двух массивов.

- Пояснение к примеру. Неотсортированная последовательность C выглядит
следующим образом:

[14, 2, 8, 18, 49, 7, 28, 63, 56, 8, 32, 72, 77, 11, 44, 99].

Отсортировав ее, получим:

[2, 7, 8, 8, 11, 14, 18, 28, 32, 44, 49, 56, 63, 72, 77, 99].

Жирным выделены первый и одиннадцатый элементы последовательности,
при этом двадцать первого элемента в ней нет. Их сумма — 51 — и будет
ответом
  
## Input / Output 

| Input                             | Output              |   
|-----------------------------------|---------------------|
| 4 4<br/>7 1 4 9<br/>2 7 8 11      | 51                  |




## Ограничения по времени и памяти

- Ограничение по времени. 2 сек.
- Ограничение по памяти. 512 мб.


## Запуск проекта
1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/haha523/algorithms-and-data-structures.git
   ```
2. **Перейдите в папку с проектом**
   ```bash
   cd "algorithms-and-data-structures/lab3"
   ```
3. **Запустить все лабораторные**
    ```bash
   python src/main.py
   ```
4. **Запустить все тесты**
    ```bash
   python -documents_count unittest discover -v
   ```
