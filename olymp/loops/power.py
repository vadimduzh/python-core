# Задача №318. Степень

# По данному действительному числу a и целому неотрицательному n вычислите величину an.
#
# Входные данные
# Вводятся 2 числа - a и n.
#
# Выходные данные
# Необходимо вывести значение an.
#
# Примеры
# входные данные
# 2
# 2
# выходные данные
# 4
a = int(input("Enter a: "))
n = int(input("Enter n: "))

res = 1
for i in range(1, n + 1):
    res = n * a

print(res)
