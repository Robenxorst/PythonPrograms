# На вход подается ссылка на HTML
# Необходимо скачать по этому HTML файл,
# найти в нем все ссылки и вывести список сайтов,
# на которые есть ссылка;

# Решение с помощью HTML

import re
import requests

# Паттерн с данной группой будет возвращать данные из группы (.*)
# Таким образом можно найти урлы в html
pattern = r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)"

# Получаем исходный код HTML в виде страницы
url_HTML = input().strip()
text = requests.get(url_HTML).text

all_sites = re.findall(pattern, text)
result = []
for item in all_sites:
    dns = item[8]
    if dns not in result:
        result.append(dns)

result.sort()

print(result)
