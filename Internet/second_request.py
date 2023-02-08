# На вход подается ссылка на HTML
# Необходимо скачать по этому HTML файл,
# найти в нем все ссылки и вывести список сайтов,
# на которые есть ссылка;


# Решение с использованием библиотеки bs4
import requests
from bs4 import BeautifulSoup

# Паттерн с данной группой будет возвращать данные из группы (.*)
# Таким образом можно найти урлы в html
pattern = r"<a.*\bhref=(?:[\"\']){0,1}(?:.*://){0,1}(\w[\w\.-]*).*"

url_HTML = input().strip()
text = requests.get(url_HTML).text
soup = BeautifulSoup(text, 'lxml')
all_sites = soup.find_all('a', class_='url') # тег a отвечает за ссылки, класс - выдает урл принадлежащий тегу 'a';
print(all_sites)
# преобразуем полученнный список в множество для исключения повторов
all_sites = set(all_sites)
# Обратное преобразование
all_sites = list(all_sites)
