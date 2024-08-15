# Задача №3064. Длина последовательности

# Внимание: В задаче нельзя использовать списки!
#
# Входные данные нужно читать до появления числа 0, означающего конец последовательности.
# Само число 0 не считается элементом последовательности и обрабатывать его не нужно.
#
# Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
# Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести
# количество членов последовательности (не считая завершающего числа 0).
#
# Подсказка: Нужно сделать бесконечный цикл while. И читать ввод данных от пользователя. Если он ввел 0, тогда выходим
# из цикла. Если нет, то берем введенной число и с делаем то, что в задаче прописано.
#
#
# Числа, следующие за числом 0, считывать не нужно.
#
# Входные данные
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит).
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# Входные данные
# 1
# 7
# 9
# 0
# Выходные данные
# 3
count = 0
while True:
    n = int(input('Enter n: '))
    if n == 0:
        break
    else:
        count += 1

print(count)
