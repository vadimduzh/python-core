# Задача №2950. Конец уроков
#
# В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д.
# уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут. Определите, когда заканчивается указанный урок.
#
# Входные данные
# Дан номер урока (число от 1 до 10).
#
# Выходные данные
# Выведите два целых числа: время окончания урока в часах и минутах. При решении этой задачи нельзя пользоваться
# циклами и условными инструкциями.
#
# Примеры
# входные данные
# 3
# выходные данные
# 11 35
# входные данные
# 2
# выходные данные
# 10 35
n = int(input("Enter the number of lesson: "))
school_break = n - 1
hours = 9
minutes = 0

if n % 2 == 0:
    minutes = minutes - 15
else:
    minutes = minutes - 5

for i in range(1, n + 1):
    if i % 2 == 0:
        minutes = minutes + 60
    else:
        minutes = minutes + 50

hours = hours + minutes // 60
minutes = minutes % 60

if hours > 12:
    res = hours % 12

    print(res, minutes)
else:
    print(hours, minutes)

