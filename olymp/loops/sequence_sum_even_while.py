# Задача №3067. Количество четных элементов последовательности
#
# Подсказка: Нужно сделать бесконечный цикл while. И читать ввод данных от пользователя. Если он ввел 0, тогда выходим
# из цикла. Если нет, то берем введенной число и с делаем то, что в задаче прописано.
#
# Определите количество четных элементов в последовательности, завершающейся числом 0.
#
# Само число 0, и все, что следует за ним, учитывать не нужно.
#
# Входные данные
# Вводится последовательность целых положительных чисел, оканчивающаяся числом 0 (само число 0 в последовательность
# не входит).
#
# Выходные данные
# Выведите ответ на задачу.
#
# Примеры
# Входные данные
# 2
# 1
# 4
# 0
# Выходные данные
# 2
count = 0
while True:
    n = int(input('Enter n: '))
    if n == 0:
        break
    elif n % 2 == 0:
        count += 1

print(count)