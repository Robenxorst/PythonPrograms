# На входе имеем два URL(A и B)
# вывести Yes если из А в В можно перейти за ДВА перехода
# иначе вывести No
# Не все ссылки внутри HTML документов ведут на существующие ресурсы

import requests
import sys
import re

# Паттерн с данной группой будет возвращать данные из группы (.*)
# Таким образом можно найти урлы в html
pattern = r"<a href=\"(.*)\".*</a>"

url_A = input()
url_B = input()
res = [] # изначально пустой результирующий список

# поиск всех урлов в А(получаем их список);
all_url_in_first = re.findall(pattern, requests.get(url_A).text)

for url in all_url_in_first:
    # поиск всех урлов по новым ссылкам
    all_url_in_second = re.findall(pattern, requests.get(url).text)
    # добавляем их в результирующий список
    res.extend(all_url_in_second)

for item in res:
    if (item == url_B):
        print("Yes")
        sys.exit() # завершение программы

print("No")