# Для заданного числа first_num проверить, является ли оно положительным.
# Если положительное, то вывести значение на экран и рядом написать Положительное
# Иначе вывести значение на экран и рядом написать Отрицательное.
first_num = 10
if first_num > 0:
    print(first_num, "This is positive num")
else:
    print(first_num, "This is negative num")

# Для заданного числа first_num проверить, является ли оно положительным.
# Если положительное, то вывести значение на экран и рядом написать Положительное
# Иначе вывести значение на экран и рядом написать Отрицательное.
second_num = -5
if second_num > 0:
    print(second_num, "This is positive num")
else:
    print(second_num, "This is negative num")

# Запросить у пользователя ввести целое число (используй функцию input) и сохранить в переменной data_1_text.
# Преобразовать data_1_text в целое число (используй функцию int) и сохранить в переменной data_1_int.
# Если data_1_int положительное, то вывести значение на экран и рядом написать Положительное
# Иначе вывести значение на экран и рядом написать Отрицательное.
data_1_text = input("Enter the num: ")
data_1_int = int(data_1_text)
if data_1_int > 0:
    print("This is positive num")
elif data_1_int == 0:
    print("This is zero")
else:
    print("This is negative num")

# Напиши программу, которая запрашивает у пользователя его возраст и выводит сообщение о том, является ли он
# совершеннолетним (18 лет и старше) или несовершеннолетним.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are adult")
else:
    print("You are not adult")
