# Задача №333. Четные числа
#
# Входные данные.
# Вводятся целые числа a и b. Гарантируется, что a не превосходит b
#
# Выходные данные
# Выведите (через пробел) все четные числа от a до b (включительно).
#
# Примеры
# входные данные
# 2
# 5
# выходные данные
# 2 4

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)

