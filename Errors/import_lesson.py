import fib
import exception
import sys

print(fib.fib(5))
print(exception.greet("Student!"))

# распечатываем путь до места где лежит модуль sys
for path in sys.path:
    print(path)