# Задача №1475. k-ая секунда суток
# Идёт k-я секунда суток. Определите, сколько целых часов h и целых минут m прошло с начала суток. Например, если
# k=13257=3*3600+40*60+57, то h=3 и m=40.
#
# Входные данные
# На вход программе подается целое число k.
#
# Выходные данные
# Выведите на экран фразу:
#
# It is ... hours ... minutes.
#
# Вместо многоточий программа должна выводить значения h
#  и m
# , отделяя их от слов ровно одним пробелом.
#
# Примеры
# Входные данные
# 13257
# Выходные данные
# It is 3 hours 40 minutes.
k = int(input("Enter k: "))

hours = k // 3600
rem_sec = k % 3600
minutes = rem_sec // 60

print("it is ", hours, "hours", minutes, "minutes")
