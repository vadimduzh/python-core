# Задача №2947. Электронные часы - 1
# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы
# в этот момент.
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках.

# Входные данные
# Вводится целое число n.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# 150
# выходные данные
# 2 30
# входные данные
# 1441
# выходные данные
# 0 1
n = int(input("Enter n: "))

hours = n // 60
minutes = n % 60
res = hours % 24

print(res, minutes)
