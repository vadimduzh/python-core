# Задача №3071. Второй максимум - 2
#
# Внимание: В задаче нельзя использовать списки!
#
# Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение второго по величине
# элемента в этой последовательности, то есть элемента, который будет наибольшим, если из последовательности удалить
# наибольший элемент.
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
# 7
# Входные данные
# 2
# 1
# 0
# Выходные данные
# 1

max_1 = -1
max_2 = -1

while True:
    num = int(input("Enter the number:"))
    if num == 0:
        break

    if num > max_1:
        max_2 = max_1
        max_1 = num
    elif max_2 == -1:
        max_2 = num

print(max_1, max_2)