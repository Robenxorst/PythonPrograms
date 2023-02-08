
def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        # кидаем исключение, если имя введенно с маленькой буквы
        raise ValueError(name + "is inappropriate name")

# создаем бесконечный цикл с условием выхода из него
while True:
    try:
        # с клавиатуры на вход поступает строка имени
        name = input("Please enter your name: ")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Please try again")
    else:
    # если исключения не происходит,
    # то мы просто выходим из цикла
        break