def get_key(d, value): # выводим ключ по значению
    for k, v in d.items():
        if v == value:
            return k

n = int(input()) # получаем на вход число вершин
# заполняем словарь значениям с клавиатуры
dict = {}
# крутим цикл n раз
while n != 0:
    # считываем список
    lst = input().split()
    name = lst[0] # первый элемнт это вершина
    lst.pop(0)  # убираем name
    # если есть предки
    if lst:
        lst.pop(0) # убираем :
    dict.update({name: lst})
    n -= 1
print(dict)

# меняем структуру словаря

# new_dict = {} # новый словарь

#for k in dict.keys(): # пробегаемся по ключам в словаре
  #  for count in dict.values():# пробегаемся по всем значениям в словаре
   #     temp = []
     #   if k == count:
       #     temp += []

