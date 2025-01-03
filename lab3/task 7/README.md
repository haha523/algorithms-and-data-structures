##  Задание 7 : Цифровая сортировка 


**Студент ИТМО,  Нгуен Хыу Жанг  415189**  

## Вариант 16

## Задание

Дано n строк, выведите их порядок после k фаз цифровой сортировки.
- Формат входного файла (input.txt). В первой строке входного файла содержатся числа n - число строк, m - их длина и k - число фаз цифровой
сортировки (1 ≤ n ≤ 10^6
, 1 ≤ k ≤ m ≤ 10^6
, n · m ≤ 5 · 10^7
). Далее
находится описание строк, но в нетривиальном формате. Так, i-ая строка
(1 ≤ i ≤ n) записана в i-ых символах второй, ..., (m + 1)-ой строк входного файла. Иными словами, строки написаны по вертикали. Это сделано
специально, чтобы сортировка занимала меньше времени
Строки состоят из строчных латинских букв: от символа "a"до символа
"z"включительно. В таблице символов ASCII все эти буквы располагаются
подряд и в алфавитном порядке, код буквы "a"равен 97, код буквы "z"равен 122.

- Формат выходного файла (output.txt). Выведите номера строк в том порядке, в котором они будут после k фаз цифровой сортировки.

- Примечание. Во всех примерах входных данных даны следующие строки:

– «bbb», имеющая индекс 1;

– «aba», имеющая индекс 2;

– «baa», имеющая индекс 3.

Разберем первый пример. Первая фаза цифровой сортировки отсортирует
строки по последнему символу, таким образом, первой строкой окажется
«aba» (индекс 2), затем «baa» (индекс 3), затем «bbb» (индекс 1). Таким
образом, ответ равен «2 3 1».
  
## Input / Output 
- Пример 1:

| Input                             | Output              |   
|-----------------------------------|---------------------|
| 3 3 1<br/>bab<br/>bba<br/>baa     | 2 3 1               |

## Input / Output 
- Пример 2:

| Input                             | Output              |   
|-----------------------------------|---------------------|
| 3 3 2<br/>bab<br/>bba<br/>baa     | 3 2 1               |


## Input / Output 
- Пример 3:

| Input                             | Output              |   
|-----------------------------------|---------------------|
| 3 3 3<br/>bab<br/>bba<br/>baa     | 2 3 1               |



## Ограничения по времени и памяти

- Ограничение по времени. 3 сек.
- Ограничение по памяти. 256 мб.


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
