# Даны два списка машин german_cars.
# С помощью среза (т.е. :) скопировать все элементы списка в новы список с именем all_cars
# Распечатать all_cars и убедиться, что вывелось ['Audi', 'BMW', 'Opel', 'Mercedes'].
german_cars = ['Audi', 'BMW', 'Opel', 'Mercedes']
all_cars = german_cars[:]
print(all_cars)

# Даны два списка машин phone_lst.
# С помощью метода списка append скопировать все элементы списка в новы список с именем my_phone_lst.
# Распечатать my_phone_lst и убедиться, что вывелось ['IPhone', 'Samsung'].
phone_lst = ['IPhone', 'Samsung']
my_phone_lst = phone_lst.copy()
print(my_phone_lst)


