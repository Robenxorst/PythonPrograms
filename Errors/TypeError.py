# Пример обработки ошибок c помощью try-exept блока

try: #кусок проверяемого кода
    x = [1, 2, 7, "Hello", 0]
    x.sort()
    print(x)
# игнорируем ошибку о сравнении двух типов
except TypeError:
    print("Type Error ;(")

print("lol")

# Таким образом появление ошибки является не критичным,
# чтобы целиком останавливать всю программу

# новый блок проверяемого кода

def divide(z, y):
    try:
        result = z / y
    except ZeroDivisionError:
        print("Univerce")
    else: #мы не словили ошибку
        print("result is", result)
    finally:
        # блок выполняющийся в любом случае
        # даже если мы словили ошибку и не смогли ее обработать
        print("finally")

divide(2, 1)
divide(2, 0)
divide(2, [])
