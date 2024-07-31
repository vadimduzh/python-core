# Задача №2961. Упорядочить три числа

# Даны три числа, записанные в отдельных строках. Упорядочите их в порядке неубывания.
#
# Программа должна считывать три числа a, b, c, затем программа должна менять их значения так, чтобы стали выполнены
# условия a <= b <= c, затем программа выводит тройку a, b, c.
#
# Входные данные
# Вводятся три числа, каждое записано в отдельной строке.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# 1
# 2
# 1
# выходные данные
# 1 1 2
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# num_lst = [a, b, c]
# max_num = num_lst[0]
# min_num = num_lst[0]
# middle_num = num_lst[0]
#
# for i in num_lst:
#     if i > max_num:
#         max_num = i
#     if i < min_num:
#         min_num = i
#
# for i in num_lst:
#     if max_num > i > min_num:
#         middle_num = i
#
# print(min_num, middle_num, max_num)
l = None
if a > b:
    l = a
    a = b
    b = l

if a > c:
    l = a
    a = c
    c = l

if b > c:
    l = b
    b = c
    c = l

print(a, b, c)
