# Дано целое число n. Выведите следующее за ним четное число.
# При решении этой задачи нельзя использовать условную инструкцию if и циклы.
#
# Входные данные
# Вводится натуральное число.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# 7
# выходные данные
# 8
# входные данные
# 8
# выходные данные
# 10
n = int(input("Enter the num: "))

print((n + 2) - (n % 2))
