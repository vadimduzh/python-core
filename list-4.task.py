# Вот тут можно посмотреть теорию: https://youtu.be/-X2ubBdP2Ak?list=RDCMUCCXF68Da_ndcmvv_9OG75Cw&t=1276

# - Пользователь вводит число с экрана и сохраняем значение в переменную num.
# - Создать список.
# - Используя функцию append добавить в список элементы 0, 1, 2, ..., num -1
# - Вывести список на экран
# lst = []
# num = int(input("Enter the number: "))
# for i in range(0, num):
#     lst.append(i)
# print(lst)

# - Пользователь вводит число с экрана и сохраняем значение в переменную num.
# - Создать список.
# - Используя функцию append добавить в список элементы 0, 1 * 10, 2 * 110, ..., (num -1) * 10
# - Вывести список на экран
# Code...
#
# lst = []
# num = int(input("Enter the number: "))
# for i in range(1, num):
#     i = i * 10
#     lst.append(i)
# print(lst)

# - Дан список lst.
# - Создать 2 новых списка lst1 и lst2
# - lst1 содержит числа меньше 10
# - lst2 содержит числа больше 10
# - вывести lst1 и lst2 на экран.
# lst = [1, 10, 2, 3, 20, 30]
# lst1 = []
# lst2 = []
# for i in lst:
#     if i <= 10:
#         lst1.append(i)
#     else:
#         lst2.append(i)
# print(lst2)
# print(lst1)

# - Дан список lst. Сложить первые 3 элемента в списке и добавить результат в lst
# Подсказка:
# - используем переменную total
# - Проходим по первым 3-м элементам lst и складываем в total
# - добавляем total в конец lst
print("START")

lst = [1, 20, 3, 40, 5]
total = 0
# ERROR: неправильно реализовано
for i in range(len(lst)):
    if i < 3:
        total = total + lst[i]
lst.append(total)
print(lst)

# - Дан список lst. Сложить первые 3 элемента в списке и добавить результат в lst
# Подсказка:
# - используем переменную total
# - Проходим по первым 3-м элементам lst и складываем в total
# - добавляем total в конец lst
lst = [1, 2, 3, 4, 5]
# ERROR: не реализовано

# - Дан список lst. Заменить первые 3 элемента на их сумму
# Подсказка:
# - После того, как посчитаешь total надо удалить первые 3 элемента
# - Потом вставить (insert) в начало списка значение total (т.е. [6, 4, 5])
print("START")
lst = [10, 12, 30, 4, 50]
total = 0

for i in lst:
    if i <= 3:
        total = total + i
        del lst[i]
lst.insert(1, total)
print(lst)
