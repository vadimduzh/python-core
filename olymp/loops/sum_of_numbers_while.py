# Задача. Сумма чисел

# По данному натуральному n сложите число 5 n раз.
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
# 3
# Выходные данные
# 15
#
# Входные данные
# 11
# Выходные данные
# 55
n = int(input("Enter n: "))

res = 0
l = 0
while l < n:
    res += 5
    l += 1

print(res)
