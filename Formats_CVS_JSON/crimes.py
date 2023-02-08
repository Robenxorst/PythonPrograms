# Вам дана частичная выборка из датасета зафиксированных преступлений,
# совершенных в городе Чикаго с 2001 года по настоящее время.
#
# Вам необходимо узнать тип преступления,
# которое было зафиксировано максимальное число раз в 2015 году(ответ THEFT)

import csv
from collections import Counter

with open('Crimes.csv') as file:
    reader = csv.reader(file)
    data = list(reader)[1:]

    # Функция zip создает из нескольких list список кортежей
    # >> > s = 'abc'
    # >> > t = (10, 20, 30)
    #
    # >> > zip(s, t)
    # [('a', 10), ('b', 20), ('c', 30)]

    # сопоставим каждому ID(первый элемент файла) свой primary type
    crimes = list(zip(*data))[5]# primary type - это пятый столбец
    # создаем счетчик данного списка
    crime_counts = Counter(crimes)

    # возвращает список из n наиболее распространенных элементов
    print(crime_counts.most_common(1))