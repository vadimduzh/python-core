# Задача №2940.
#
# Длина кольцевой автомобильной дороги 109 километров.
# Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v километров в час.
# На какой отметке он остановится через t часов?
#
# Входные данные
# Программа получает на вход значения v и t.
# Если v > 0, то Вася движется в положительном направлении по МКАД, если же значение v<0, то в отрицательном.
#
# Выходные данные
# Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановится Вася.
#

# Примеры
#
# входные данные
# 20
# 3
# выходные данные
# 60
# входные данные
# 60
# 2
# выходные данные
# 11
#
# входные данные
# -1
# 1
# выходные данные
# 108

v = int(input("Enter v: "))

if v < 0:
    v = v * -1

t = int(input("Enter t: "))

s = v * t

if s > 109:
    print(s - 109)
else:
    print(109 - s)
