def C(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return C(n-1, k) + C(n-1, k-1)

n, k = map(int, input().split())
# input возвращает строку(например "1 2 3")
# split() преобразует строку в list по разделителю
# map преобразует список в соответствие с функцией
f = C(n, k)
print(f)