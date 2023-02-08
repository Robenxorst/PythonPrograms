class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            # обращаемся к предку нашего класса, т.е. к list
            # чтобы избежать бесконечной рекурсии
            super().append(x)
        else:
            raise NonPositiveError(str(x) + " is not positive!")

y = PositiveList()
y.append(2)
y.append(2)
y.append(2)
print(y)
y.append(-2)
print(y)