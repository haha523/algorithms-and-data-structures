##  Задание 6 : Поиск максимальной прибыли 

**Студент ИТМО,  Нгуен Хыу Жанг  415189**  

## Вариант 16

## Задание
Используя псевдокод процедур Find Maximum Subarray и Find Max Crossing
Subarray из презентации к Лекции 2 (страницы 25-26), напишите программу поиска максимального подмассива.
Примените ваш алгоритм для ответа на следующий вопрос. Допустим, у нас
есть данные по акциям какой-либо фирмы за последний месяц (год, или иной срок).

Проанализируйте этот срок и выдайте ответ, в какой из дней при покупке единицы
акции данной фирмы, и в какой из дней продажи, вы бы получили максимальную
прибыль? Выдайте дату покупки, дату продажи и максимальную прибыль.
Вы можете использовать любые данные для своего анализа. Например, я набрала в Google "акции" и мне поиск выдал акции Газпрома, тут - можно скачать
информацию по стоимости акций за любой период. (Перейдя по ссылке, нажмите
на вкладку "Настройки"→ "Скачать")
Соответственно, вам нужно только выбрать данные, посчитать изменение цены и применить алгоритм поиска максимального подмассива.
- Формат входного файла в данном случае на ваше усмотрение.
- Формат выходного файла (output.txt). Выведите название фирмы, рассматриваемый вами срок изменения акций, дату покупки и дату продажи
единицы акции, чтобы получилась максимальная выгода; и сумма этой прибыли.

 
## Input / Output 


| Input                                                                                     | Output                                                                                 |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Gazprom<br/>2024-09-01 2024-09-02 2024-09-03 2024-09-04 2024-09-05<br/>100 180 260 310 40 | Company: Gazprom<br/>Buy on: 2024-09-02<br/>Sell on: 2024-09-04<br/>Max Profit: 210.0  |




## Ограничения по времени и памяти


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
   python src/main.py
   ```
4. **Запустить все тесты**
    ```bash
   python -documents_count unittest discover -v
   ```
