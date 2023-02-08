class MoneyBox:
    def __init__(self, capacity = 0):
        self.cap = capacity # вместимость копилки
        self.count = 0 # количество монет в копилке равно 0 при инициализации
    def can_add(self, v):#проверка, что мы можем положииь монеты в копилку
        if (self.cap - self.count >= v):
            return True
        return False
    def add(self, v):
        if (self.can_add(v) == True):
            self.count += v
            return True
        else:
            print("The MoneyBox is full\n")
            return False

money = MoneyBox(10)
if(money.can_add(5) == True):
    money.add(5)
print(money.count)
if(money.can_add(10) == True):
   money.add(10)
else:
  print("No money, no honey\n")
print(money.count)

