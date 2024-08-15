# Задача №3075. Номер числа Фибоначчи
#
#
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите
# такое число n, что φn=A. Если А не является числом Фибоначчи, выведите число -1.
#
# Входные данные
# Вводится натуральное число.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# Входные данные
# 8
# Выходные данные
# 6
# Входные данные
# 10
# Выходные данные
# -1
A = int(input("Enter A: "))

# Решение Вадим
f_1 = 0
f_2 = 1
i = 1
while f_2 < A:
    f = f_1 + f_2
    f_1 = f_2
    f_2 = f
    i += 1

if A == f_2:
    print(i)
elif A < f_2:
    print(-1)

# Решение папа
f_1 = 0
f_2 = 1
# номер последнего числа фибоначчи
i = 1
while True:
    # считаем число Фибоначчи для i
    i = i + 1
    f = f_1 + f_2

    if A == f:
        # если совпадает с A, то печатаем i и выходим
        print(i)
        break
    elif A < f:
        # если больше A, то печатаем -1 и выходим
        print(-1)
        break
    else:
        # если меньше A, то считаем следующее число
        f_1 = f_2
        f_2 = f