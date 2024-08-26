# Задача №107. Самое длинное слово
#
# Дана строка, содержащая пробелы. Найдите в ней самое длинное слово, выведите это слово и его длину.
# Если таких слов несколько, выведите первое из них.
#
# Код должен содержать 2 решения:
# - используя встроенную функцию split для строки
# - свое решение. Можно сделать так, как было в задачах по while: завести переменные, которые содержат самое длинное
# слово, ну и текущее слово (это слово мы считаем проходя по символам). Через цикл for пройти по всем символами и
# записывать текущее слово в переменную. Если значение в переменной "текущее слово" становится больше макисмального,
# то перезаписываем его в максимальное. Если текущий символ - это пробел, тогда в переменную "текущее слово" заносим
# пусто. Если есть другие варианты решения, то можете их написать
#
# Входные данные
# Задана одна строка, содержащая пробелы. Слова разделены ровно одним пробелом. Пробелы в начале и конце строки
# не допускаются.
#
# Выходные данные
# Необходимо вывести самое длинное слово в строке и его длину.
#
# Примеры
# входные данные
# one two three four five six
# выходные данные
# three
# 5
s = input("Enter s: ")
world_lst = s.split()

max_1 = world_lst[0]
max_len = len(world_lst[0])
for i in world_lst:
    if len(i) > max_len:
        max_len = len(i)
        max_1 = i

print(max_1, max_len)

# list_1 = []
# count_1 = 0
# for i in s:
#     while i != " ":
#         count_1 += 1
#         if i == " ":
#             list_1.append(count_1)
#             count_1 = 0
#         break
#
# print(list_1)
