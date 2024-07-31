# Задача №301. Квадратное уравнение

# Даны действительные числа a, b, c. Найдите все решения квадратного уравнения ax2 + bx + c = 0.
#
# Входные данные
# Даны три действительных числа, a не равно 0.
#
# Выходные данные
# Выведите два действительных числа в любом порядке, если уравнение имеет два корня, одно действительное число –
# при наличии одного корня. При отсутствии действительных корней ничего выводить не нужно.
#
# Примеры
# входные данные
# 1
# 0
# 0
# выходные данные
# 0
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b**2 - 4 * a * c

if d < 0:
    print()
else:
    x_1 = (-b + d**0.5) / 2 * a
    x_2 = (-b - d**0.5) / 2 * a

    if x_2 == x_1:
        print(x_1)
    else:
        print(x_1, x_2)