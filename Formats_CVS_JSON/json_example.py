# JSON - Java Script Object Annotation(аннотация объектов языка JavaScript)
# Объекты в Java ведут себя так же как и словари - они хранят в себе пару ключ-значение;
# При этом ключом в json объекте может быть только строка, None соответсвует значению null

import json

student1 = {
    "first_name": "Oleg",
    "last_name": "Dean",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Good job, Greg"
}
student2 = {
    "first_name": "Wirl",
    "last_name": "Wood",
    "certificate": True,
    "scores": [
        70,
        80.2,
        90
    ],
    "description": "Nicely Done"
}
data = [student1, student2]

# Запись данных в файл(открываем его на чтение);
# with open("students.json", "w") as f:
#     json.dump(data, f, indent=4, sort_keys=True)

# создание данных из формата json
data_json = json.dumps(data, indent=4, sort_keys=True)
data_again = json.loads(data_json)
# хотим получить сумму баллов первого студента
print(sum(data_again[0]["scores"]))

with open("students.json", "r") as f:
    new_data = json.load(f) # загружаем данные из файла loads
    # получаем сумму баллов второго студента
    print(sum(data_again[1]["scores"]))