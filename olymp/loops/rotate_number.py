# Задача №338. Переверни число
#
#
# Входные данные
# Вводится натуральное число x
#
# Выходные данные
# Выведите число, состоящее из цифр данного числа x в обратном порядке. Ведущие нули выводить не нужно.
#
# Примеры
#
# Входные данные
# 12345
# Выходные данные
# 54321
#
# Входные данные
# 12300
# Выходные данные
# 321
x = input("Enter x: ")

# решение один
num = int(x)
lst = []

for i in range(len(x)):
    rem = num % 10
    lst.append(str(rem))
    num = num // 10

s = "".join(lst)
res = int(s)
print(res)

# решение два
s_1 = ""
for el in x:
    s_1 = el + s_1

res_1 = int(s_1)
print(res_1)

# решение три
s_2 = x[::-1]
res_2 = int(s_2)
print(res_2)
