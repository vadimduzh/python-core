# Вызвать функцию print со строкой Hello World!
print("Hello world")

# Задать переменную hello_str и ей присвоить строку Hello World!
# Затем вызвать функцию print с переменной hello_str в качестве параметра
hello_str = "Hello world"
print(hello_str)


# Написать свою функцию my_fn с двумя аргументами (они же параметрами) a и b.
# В теле функции сложить a и b, а значение сохранить в переменной c. Значение с вернуть через return.
# Вызвать функцию my_fn c параметрами 10 и 20 и значение сохранить в переменной my_fn_result
# Затем вызвать функцию print с переменной my_fn_result в качестве параметра

def my_fn(a, b):
    c = a + b
    return c

my_fn_result = my_fn(10, 20)

print(my_fn_result)


# Попросить пользователя ввести имя в терминале с помощью функции input.
# Значение записать в переменную my_name_str
# Затем вызвать функцию print с переменной my_name_str в качестве параметра
my_name_str = input("Enter your name: ")
print(my_name_str)
