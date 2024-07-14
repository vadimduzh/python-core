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
t = int(input("Enter t: "))

s = v * t

if s >= 0:
    reminder_value = s % 109
    res = 0 + reminder_value
else:
    reminder_value = (s * -1) % 109
    res = 109 - reminder_value

print(res)
