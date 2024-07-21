# Задача №254. Ладья
#
# Требуется определить, бьет ли ладья, стоящая на клетке с указанными координатами (номер строки и номер столбца),
# фигуру, стоящую на другой указанной клетке.
#
# Входные данные
# Вводятся четыре числа: координаты ладьи (два числа) и координаты другой фигуры (два числа), каждое число вводится в
# отдельной строке. Координаты - целые числа в интервале от 1 до 8.
#
# Выходные данные
# Требуется вывести слово YES, если ладья сможет побить фигуру за 1 ход и NO - в противном случае.
#
# Примеры
# входные данные
# 1
# 1
# 2
# 2
# выходные данные
# NO
# входные данные
# 1
# 1
# 2
# 1
# выходные данные
# YES
x_1 = int(input("Enter first coordinate: "))
y_1 = int(input("Enter second coordinate: "))
x_2 = int(input("Enter third coordinate: "))
y_2 = int(input("Enter fourth coordinate: "))

if x_2 <= 8 and y_2 == y_1 or y_2 <= 8 and x_2 == x_1:
    print("YES")
else:
    print("NO")
