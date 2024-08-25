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
count = 0

if s_1 == s_2:
    print(1, "yes")
else:
    print(1, "no")

if len(s_1) != len(s_2):
    print(2, "no")
else:
    # all
    res = True
    for i in range(len(s_1)):
        res = res and (s_1[i] == s_2[i])
        if not res:
            break
    print(4, res)

#     for i in range(len(s_1)):
#         if s_1[i] != s_2[i]:
#             print(2, "no")
#             break
#         if s_1[i] == s_2[i]:
#             count += 1
#
# if count == len(s_1):
#     print(2, "yes")
