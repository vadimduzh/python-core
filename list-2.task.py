# Вот тут можно посмотреть теорию: https://youtu.be/-X2ubBdP2Ak?list=RDCMUCCXF68Da_ndcmvv_9OG75Cw

# - Дан список. Вывести на экран каждый элемент списка используя цикл for
lst = [1, 2, 3, 4, 5]
for i in lst:
    print(i)

# - Дан список. Вывести на экран каждый элемент списка используя цикл while
lst = [10, 20, 30, 40, 50]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

# - Дан список. Вывести на экран каждый элемент списка умноженный на 10 используя цикл for
lst = [10, 20, 30, 40, 50]
lst1 = []
for i in lst:
    i = i * 10
    lst1.append(i)
print(lst1)

# - Дан список. Вывести на экран каждый элемент списка умноженный на 10 используя цикл while
lst = [10, 20, 30, 40, 50]
i = 0
while i < len(lst):
    print(lst[i] * 10)
    i += 1

# - Дан список. Вывести на экран те элементы списка, которые меньше 5.
# - Используем цикл for для прохода по списку и if для проверки
lst = [10, 2, 3, 7, 6]
for i in lst:
    if i < 5:
        print(i)



