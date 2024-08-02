# Задача №317. Число сочетаний

# По данным натуральным n и k вычислите значение C=n!/(k!(n−k)!) (число сочетаний из n элементов по k).
# n! - это факториал числа n, который мы уже писали в задаче из раздела arithmetic

# Подсказка: Здесь факториал считается несколько раз - для n, k и n−k. Чтобы не писать один и тот же код 3 раза,
# советую написать функцию factorial, котора принимает парамер num и возвращает факторил этого числа. А потом вы просто
# ее вызовете 3 раза и посчитаете C.

#
# Входные данные
# Вводятся 2 числа - n и k (n, k≤10).
#
# Выходные данные
# Необходимо вывести  значение C
# .
#
# Примеры
# Входные данные
# 2
# 1
# Выходные данные
# 2
n = int(input("Enter n: "))
k = int(input("Enter k: "))


def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res


# C=n!/(k!(n−k)!)
total = factorial(n) / (factorial(k) * factorial(n - k))

print(total)
