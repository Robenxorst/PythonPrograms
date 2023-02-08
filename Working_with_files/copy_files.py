# Безопасная функция копирования содержимого одного файла в другой

with open("test_append.txt", "r") as f, open("test_cp.txt", "w") as w:
    for line in f:
        w.write(line)