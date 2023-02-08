# В этой задаче вам необходимо воспользоваться API
# сайта artsy.net. API проекта Artsy предоставляет информацию о некоторых
# деятелях искусства, их работах, выставках. Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Имена выводим в порядке возрастания года рождения

import requests
import json

# получение токена доступа на сайте
client_id = '9e89fe49d93594464667'
client_secret = '422fcf9c43a8473848828d2c2e55bd14'

# инициируем запрос на получение токена
req = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(req.text)
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

dictonary = {}
with open('test.txt') as file:
    for string in file:
        string = string.strip()
        # операция format подставляет вместо {} number
        url = 'https://api.artsy.net/api/artists/{}'.format(string)
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        data = json.loads(res.text)
        dictonary[data['sortable_name']] = data['birthday']

    sort_dictonary = sorted(dictonary.items(), key=lambda x: (x[1], x[0]))
    for artists in sort_dictonary:
        print(artists[0])