# Задача №336. Цифра в числе
#
# Входные данные.
# Вводятся 2 числа: x и d.
#
# Выходные данные.
# Подсчитайте и выведите одно число - сколько раз встречается в записи натурального числа x цифра d.
x = input("Enter x:")
d = int(input("Enter y:"))

res = 0
for i in x:
    if int(i) == d:
        res += 1

print(res)
