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
print(sum_nums((100, 10), "Зарплата: ",)
#НЕПРАВИЛЬНО ПОСТАВЛЕНА ЗАДАЧА, В НЕЙ ГОВОРИТЬСЯ ЧТО ТРЕТЬИМ ПАРАМЕТРОМ ДОЛЖНА БЫТЬ СТРОКА, ОДНАКО У НАС В ФУНКЦИИ НАСЧИТЫВАЕТСЯ ТОЛЬКО 2 ПАРАМЕТРА!!!!


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
