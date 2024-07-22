# Задача №259. Фишки
#
# В каждую крайнюю клетку квадратной доски поставили по фишке. Могло ли оказаться, что выставлено ровно k
#  фишек? (Например, если доска 2×2, то выставлено 4 фишки, а если 6×6  - то 20).
#
# Входные данные
# Вводится одно натуральное число k, не превосходящее 30000
#
# Выходные данные
# Программа должна вывести слово YES, если существует такой размер доски, на который будет выставлено ровно
# (не больше, и не меньше) k фишек, в противном случае - вывести слово NO.
#
# Примеры
# входные данные
# 20
# выходные данные
# YES
# входные данные
# 13
# выходные данные
# NO
k = int(input("Enter k: "))

if k % 4 == 0:
    print("YES")
else:
    print("NO")
