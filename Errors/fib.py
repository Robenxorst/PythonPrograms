# медленная рекурсивная обработка числа Фиббоначчи

def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

# блок вычисления с предотвращением ненужного импорта
if __name__ == "__main__":
    print(__name__)
    print(fib(31))