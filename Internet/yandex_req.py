# Усли мы запрашиваем информацию у поисковика,
# то с помощью флага search после домена можно задать текстовый запрос к поисковику

import requests

# Большие url запросы лучше составлять с помощью сторонней библиотеки!
# Так же есть отдельный метод post, который меняет содержимое веб-ресурса
res =requests.get("https://yandex.ru/search/", params={"text": "Stepic"})
print(res.status_code)
print(res.url)
print(res.text)