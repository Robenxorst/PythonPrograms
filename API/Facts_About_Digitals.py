# Воспользуемся API сайта numbersapi.com.
# Вам дается набор чисел. Для каждого из чисел необходимо узнать,
# существует ли интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт,
# и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.


import requests
import json

with open('test.txt') as file:
    for number in file:
        number = number.strip()
        params = {'default': 'Boring number is boring', 'json': True}
        # операция format подставляет вместо {} number
        url = 'http://numbersapi.com/{}/math'.format(number)
        res = requests.get(url, params=params).text
        data = json.loads(res)
        if 'Boring' in data['text']:
            print('Boring')
        else:
            print('Interesting')