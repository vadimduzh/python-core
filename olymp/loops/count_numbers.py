# Задача №346. Подсчет чисел
#
# Подсчитайте, сколько среди данных N чисел нулей, положительных чисел, отрицательных чисел.
#
# Входные данные
# Вводится число N, а затем N целых чисел.
#
# Выходные данные
# Необходимо вывести сначала число нулей, затем число положительных и отрицательных чисел.
#
# Примеры
# Входные данные
# 5
# 28
# 0
# 0
# 0
# 0
# Выходные данные
# 4 1 0
# Входные данные
# 10
# 1
# -1
# 0
# 2
# -3
# -4
# 0
# 0
# 0
# 0
# Выходные данные
# 5 2 3
N = int(input("Enter the count of nums: "))

num_list = []
for i in range(0, N):
    n = int(input("Enter: "))
    num_list.append(n)

zero = 0
positive_num = 0
negative_num = 0
for i in num_list:
    if i == 0:
        zero += 1
    elif i > 0:
        positive_num += 1
    else:
        negative_num += 1

print(zero, positive_num, negative_num)
