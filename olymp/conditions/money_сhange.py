# Задача №262. Сдача
#
# Товар стоит a руб. b коп. За него заплатили c руб. d коп. Сколько сдачи требуется получить?
#
# Входные данные
# Вводятся 4 числа: a, b, c и d.
#
# Выходные данные
# Необходимо вывести 2 числа: e и f, число рублей и копеек, соответственно.
#
# Примеры
# входные данные
# 5
# 5
# 6
# 5
# выходные данные
# 1 0
# входные данные
# 2
# 17
# 2
# 18
# выходные данные
# 0 1
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

sum_1 = b + a * 100
sum_2 = d + c * 100

bun = (sum_2 - sum_1) // 100
coins = (sum_2 - sum_1) % 100

print(bun, coins)
