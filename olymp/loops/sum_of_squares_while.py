# Задача №315. Сумма квадратов

# По данному натуральному n вычислите сумму 1**2 + 2**2 +... + n**2.
# Используйте цикл while
#
# Входные данные
# Вводится единственное натуральное число n, не превосходящее 100
#
# Выходные данные
# Необходимо вывести вычисленную сумму.
#
# Примеры
# Входные данные
# 2
# Выходные данные
# 5
n = int(input("Enter n: "))

k = 1
res = 0

while k <= n:
    res += k ** 2
    k += 1

print(res)