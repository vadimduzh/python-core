# Задача №265. Котлеты
#
# На сковородку одновременно можно положить k  котлет. Каждую котлету нужно с каждой стороны обжаривать m минут
# непрерывно. За какое наименьшее время удастся поджарить с обеих сторон n котлет?
#
# Входные данные
# Вводятся 3 числа: k, m и n. Все числа не превосходят 32000.
#
# Выходные данные
# Вывести время, за которое все котлеты будут обжарены.
#
# Примеры
# входные данные
# 1
# 5
# 1
# выходные данные
# 10
k = int(input("Enter k: "))
m = int(input("Enter m: "))
n = int(input("Enter n: "))

time = 0
plate = (n // k) + (n % k)
time = plate * m * 2

print(time)

