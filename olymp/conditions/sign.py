# Задача №2959. Знак числа
#
# В математике функция sign(x) (знак числа) определена так:
# sign(x) = 1,   если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0,   если x = 0.
#
# Для данного числа x выведите значение sign(x).
# Входные данные
# Вводится число x.
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# входные данные
# 179
# выходные данные
# 1
x = int(input("Enter x: "))
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)
