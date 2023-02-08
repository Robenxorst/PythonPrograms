# На основе заданного файла генерируем файл
# с реверсированными строками

with open("test_append.txt", "r") as f, open("test_cp.txt", "w") as w:
    x = f.read()  # считали все в х
    y = x.splitlines() # разбиение текста на строки(в виде списка)
    print(y)
    y.reverse()
    print(y)
    contents = "\n".join(y)
    w.write(contents)