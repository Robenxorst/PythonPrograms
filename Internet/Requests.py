import requests

# получаем response object - класс с описанием ответа сервера
res = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res.status_code)
# Все хедеры доступны в качестве словаря
print(res.headers['Content-Type'])
# Получение тела ответа сервера
print(res.content)
# Если мы уверены, что запрашиваем текстовые данные
# print(res.text)

# Сохранение полученной бинарной информации в файл(можем записать изображение)

with open("python.png", "wb") as f: # wb - запись бинарных данных;
    f.write(res.content)