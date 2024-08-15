# Задача №3065. Сумма последовательности

# Определите сумму всех элементов последовательности, завершающейся числом 0.
#
# Подсказка: Нужно сделать бесконечный цикл while. И читать ввод данных от пользователя. Если он ввел 0, тогда выходим
# из цикла. Если нет, то берем введенной число и с делаем то, что в задаче прописано.
#
#
# Числа, следующие за нулем, считывать не нужно.
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
# 17
count = 0
while True:
    n = int(input('Enter n: '))
    if n == 0:
        break
    else:
        count += n

print(count)
