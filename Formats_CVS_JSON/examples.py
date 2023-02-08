# CSV - common separeted values
# (табличный формат данных или значения разделенные запятой);
# идеален для таблиц
# " - обосабливают символы на отдельные элементы

import csv

with open("example.csv") as f:
    # итерируемый конструктор reader
    reader = csv.reader(f)
    for row in reader:
        print(row)
# аналогично можно считывать файл построчно
# и делать split по запятой, однако это не рекомендуется

# запись в csv файл
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example.csv", "a") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)# хотим поместить в кавычки все символы на записи
    # можно проще: writer.writerows(students)
    for student in students:
        writer.writerow(student)