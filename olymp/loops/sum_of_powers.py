# Задача №353. Сумма степеней
#
# Входные данные
# Вводится натуральное число N, которое не превосходит 30.
#
# Выходные данные
# Вычислите 1+2+2**2+2**3+…+2**N.
#
# Примеры
# входные данные
# 4
# выходные данные
# 31
n = int(input("Enter n: "))

res = 1
for i in range(1, n + 1):
    res = res + 2**i

print(res)
