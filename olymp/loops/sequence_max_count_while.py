# Задача №3072. Количество элементов, равных максимуму
#
# Внимание: В задаче нельзя использовать списки!
#
# Последовательность состоит из натуральных чисел и завершается числом 0. Всего вводится не более 10000 чисел
# (не считая завершающего числа 0).
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Входные данные
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# Входные данные
# 1
# 7
# 9
# 0
# Выходные данные
# 1
# Входные данные
# 1
# 3
# 3
# 1
# 0
# Выходные данные
# 2
count_max = 0
max_num = -1
while True:
    n = int(input('Enter n: '))
    if n == 0:
        break

    if n > max_num:
        max_num = n
        count_max = 1
    elif n == max_num:
        count_max += 1

print(count_max)