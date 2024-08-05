# Задача №321. Сумма - 2

# По данному числу n вычислите сумму 4*(1-1/3+1/5-1/7+...+(-1)**n/(2n+1)).
#
# Входные данные
# Вводится одно число n, не превосходящее 100000.
#
# Выходные данные
# Необходимо вывести  значение выражения.
#
# Примеры
# входные данные
# 1
# выходные данные
# 2.66667
n = int(input("Enter n: "))

res = 0
for i in range(0, n + 1):
    res = res + ((-1)**i / (2 * i + 1))
res *= 4

print(res)
