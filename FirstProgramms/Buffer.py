## Класс буфера, которому на вход приходят произвольные списки чисел.
# Распечатываются первые 5 чисел , потом буфер чиститься.

class Buffer:
    def __init__(self):
        self.lst = list()# список хранимых чисел
        self.count = 0# счетчик, отвечающий за количество чисел в списке
    def add(self, *a):
        for elem in a: ## пока есть элементы во входном массиве
            self.count += 1## увеличиваем счетчик
            self.lst.append(elem) ## добавляем элемент в массив
            if (self.count == 5): ## если в массиве пять элементов
                # считаем их сумму(из 5ти элементов)
                sum = 0
                for k in self.lst:
                    sum += k
                print(sum)# распечатываем сумму 5ти элементов
                ## удаляем все элементы из списка
                self.lst.clear()
                ## обнуляем счетчик
                self.count = 0
    def get_current_part(self):
        return self.lst

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]