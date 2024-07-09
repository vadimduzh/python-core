# Объявить функцию sum_nums с двумя параметрами a и b
# В блоке кода нужно сложить a и b, а результат присвоить переменной sum. Затем sum вернуть из функции.
def sum_nums(a, b):
    sum = a + b
    return sum


# Вызвать функцию sum_nums с параметрами 100 и 200, и присвоить переменной first_sum
# Распечатать first_sum
# Т.е. должно вывести: 300
first_sum = sum_nums(100, 200)
print(first_sum)

# Вызвать функцию sum_nums с параметрами 24.99 и 25.01, и присвоить переменной second_sum
# Распечатать second_sum
# Т.е. должно вывести: 100
second_sum = sum_nums(24.99, 25.01)
print(second_sum)

# Передать вызов функции sum_nums с параметрами 300 и 10 в функцию print
# Т.е. должно вывести: 310
print(sum_nums(300, 10))

# Передать вызов функции sum_nums с параметрами 50 и 10 в функцию print первым параметром, а вторым строку BYN
# Т.е. должно вывести: 60 BYN
print(sum_nums(50, 10), "BYN")

# Передать вызов функции sum_nums с параметрами 100 и 10 в функцию print первым параметром,
# а вторым строку Зарплата:, а третьим USD.
# Т.е. должно вывести: Зарплата: 110 USD
print("Зарплата:", sum_nums(100, 10), "USD")

# Вызвать функцию sum_nums с параметрами, которые являются вызовами функции sum_nums.
# Первый параметр: sum_nums с параметрами 100 и 200
# Второй параметр: sum_nums с параметрами 300 и 400
# Значения вызова первой sum_nums присвоить third_sum
# Распечатать third_sum
# Т.е. должно вывести: 1000

third_sum = sum_nums(sum_nums(100, 200), sum_nums(300, 400))
print(third_sum)


# Объявить функцию hello без параметров
# В блоке кода объявить переменную и присвоить ей 1. return не используется.
# Вызвать функцию hello и присвоить переменной hello_value
# Распечатать hello_value
# Т.е. должно вывести: None

def hello():
    num = 1


hello_value = hello()
print(hello_value)


# Объявить функцию my_max с параметром num_lst, который содержит список чисел. Функция находит максимальное значение
# в списке и возвращает его.
# Примечание: В блоке кода нужно пройти по списку и найти максимальное значение и сохранить его в переменной max_value.
# Затем max_value вернуть из функции.
def my_max(num_lst):
    max_value = num_lst[0]
    for num in num_lst:
        if num > max_value:
            max_value = num
    return max_value


# Вызвать функцию my_max с параметрами [10, 5, 5, 6, 11] и сохранить результат в переменной max_res.
# Вывести max_res на экран и убедиться, что там 11.
max_res = my_max([10, 5, 5, 6, 11])
print("max_res:", max_res)

# Вызвать функцию my_max с параметрами [15, 1, 6] и сохранить результат в переменной max_res.
# Вывести max_res на экран и убедиться, что там 15.
max_res = my_max([15, 1, 6])
print("max_res:", max_res)


# Объявить функцию my_min с параметром num_lst, который содержит список чисел. Функция находит минимальное значение
# в списке и возвращает его.
def my_min(num_lst):
    min_value = num_lst[0]
    for num in num_lst:
        if num < min_value:
            min_value = num
    return min_value


# Вызвать функцию my_min с параметрами [10, 5, 5, 6, 11] и сохранить результат в переменной min_res.
# Вывести min_res на экран и убедиться, что там 5.
min_res = my_min([10, 5, 5, 6, 11])
print("min_res:", min_res)

# Вызвать функцию my_min с параметрами [15, 1, 6] и сохранить результат в переменной min_res.
# Вывести min_res на экран и убедиться, что там 1.
min_res = my_min([15, 1, 6])
print("min_res:", min_res)


# Объявить функцию my_mun с параметром num_lst, который содержит список чисел. Функция находит сумму всех значений
# в списке и возвращает ее.
def my_sum(num_lst):
    sum = 0
    for num in num_lst:
        sum = sum + num
    return sum


# Вызвать функцию my_sum с параметрами [10, 9, 11] и сохранить результат в переменной sum_res.
# Вывести sum_res на экран и убедиться, что там 30.
sum_res = my_sum([10, 9, 11])
print("sum_res:", sum_res)

# Вызвать функцию my_sum с параметрами [13, 1, 6] и сохранить результат в переменной sum_res.
# Вывести sum_res на экран и убедиться, что там 20.
sum_res = my_sum([13, 1, 6])
print("sum_res:", sum_res)


# Написать функцию index_in_list, которая возвращает индекс буквы в массиве букв.
# Функция принимает 2 параметра:
# - letter_lst - список букв
# - letter - искомая буква
# Функция возвращает индекс буквы в списке letter_lst или значение -1, если буквы letter нет в списке letter_lst.
#
# Подсказка: в теле функции нужно с помощью индексов пройти по циклу letter_lst и проверить, совпадает ли буква по
# индексу с параметром letter. Если да, то вернуть индекс из функции. Если нет, то вернуть -1.
# Есть такой прием: перед циклом завести переменную letter_ind и занести в нее значение None, т.е. ничего. Потом идем
# по циклу по индексу, и если значение по индексу совпадает, тогда в letter_ind заносим текущий индекс.
# Когда цикл закончится, то в letter_ind будет или None или правильный индекс. Нужно проверить letter_ind - если оно
# равно None, то тогда вернуть -1. Иначе вернуть то, что лежит в letter_ind.
def index_in_list(letter_lst, letter):
    letter_ind = None

    for i in range(len(letter_lst)):
        if letter_lst[i] == letter:
            letter_ind = i

    if letter_ind is None:
        return -1
    else:
        return letter_ind


my_res = index_in_list(["a", "b", "c"], "b")
print("Index:", my_res)
