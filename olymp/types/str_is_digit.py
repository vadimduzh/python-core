# Задача №102. Проверить, является ли символ цифрой
#
# Напишите программу, определяющую, является ли данный символ цифрой или нет.
#
# Код должен содержать 2 решения:
# - используя встроенную функцию isdigit для строки
# - свое решение, т.е разобрать строку и посмотреть число или нет.
#
# Входные данные
# Задан единственный символ c.
#
# Выходные данные
# Необходимо вывести  строку yes, если символ является цифрой, и строку no в противном случае.
#
# Примеры
# Входные данные
# c
# Выходные данные
# no
# Входные данные
# 2
# Выходные данные
# yes
c = input("Enter the symbol: ")
print(c.isdigit())


if (int(c) == 0 or int(c) == 1 or int(c) == 2 or int(c) == 3 or int(c) == 4 or int(c) == 5
        or int(c) == 6 or int(c) == 7 or int(c) == 8 or int(c) == 9):
    print("yes")
else:
    print("no")
