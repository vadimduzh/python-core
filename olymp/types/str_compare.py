# Задача №105. Совпадают ли строки?
#
# Напишите программу, определяющую, совпадают ли 2 строки.
#
# Код должен содержать 2 решения:
# - используя оператор ==
# - свое решение
#
# Входные данные
# Заданы 2 строки.
#
# Выходные данные
# Необходимо вывести  слово yes, если строки совпадают, и слово no в противном случае.
#
# Примеры
# Входные данные
# a
# a
# Выходные данные
# yes
s_1 = input("Enter the first symbol: ")
s_2 = input("Enter the second symbol: ")

if s_1 == s_2:
    print("yes")
