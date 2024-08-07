# Задача №304. Б
# илеты на метро

# Билет на одну поездку в метро стоит 15 рублей, билет на 10 поездок стоит 125 рублей, билет на 60 поездок стоит 440
# рублей. Пассажир планирует совершить n поездок.
#
# Определите, сколько билетов каждого вида он должен приобрести, чтобы суммарное количество оплаченных поездок было
# не меньше n, а общая стоимость приобретенных билетов – минимальна.
#
# Входные данные
# Дано одно число n - количество поездок.
#
# Выходные данные
# Выведите три целых числа, равные необходимому количеству билетов на 1, на 10, на 60 поездок.
#
# Примеры
# входные данные
# 129
# выходные данные
# 0 1 2

# total trips
n = int(input("Enter n: "))

ticket_60_count = ticket_10_count = ticket_1_count = 0

ticket_60_count = n // 60
trips = n % 60

ticket_10_count = trips // 10
trips = trips % 10

if trips > 0:
    if trips * 15 > 125:
        ticket_10_count += 1
    else:
        ticket_1_count = trips

print(ticket_1_count, ticket_10_count, ticket_60_count)
