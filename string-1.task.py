#  теория тут: https://www.youtube.com/watch?v=pqaBWcsBGyA&list=RDCMUCCXF68Da_ndcmvv_9OG75Cw

# Дана строка s. Вывести на экран 3-й и 7-й символ строки (по индексу)
s = "Hello World!"
print(s[2])
print(s[6])

# Дана строка s. Вывести длину строки
s = "Hello World!"
print(len(s))

# Дана строка s. Посчитать количество букв l в строке
s = "Hello World!"
count = 0
for i in s:
    if i == "l":
        count = count + 1
print(count)
# Дана строка s. Вывести на экран строку в:
# - верхнем регистре ("HELLO WORLD!")
# - нижнем регистре ("hello world!")
# - Первая буква заглавная, а остальные маленькие ("Hello world!")
s = "Hello World!"
s = s.upper()
print(s)
s = s.lower()
print(s)

# Дана строка s. Вывести на эран все ли буквы в ней в верхнем регистре
s = "Hello World"
s1 = s.upper()
# Error: неправильно сделано.

# Дана строка s. Вывести на эран все ли буквы в ней в нижнем регистре
s = "hello world"
# Error: не сделано.

# Дана строка s. Найти индекс символа W в строке s и вывести на экран
s = "Hello World!"
print(s.index("W"))

# Дана строка s. Есть ли символ x в строке s (использвать find)
s = "Hello World!"
a = s.find("x")
if a == -1:
    print(False)
else:
    print(True)

# Дана строка s. Разделить строку на куски (split) и вывести на экран имена
s = "Denis, Vadim, Maxim"
print(s.split())

# Дана список имен. Объеденить имена в строку s с разделителем ", ". Распечатать s
ls = ["Denis, Vadim, Maxim"]
join = ", ".join(ls)
print(join)


# Дана строка s. С помощью среза получить кусок строки, что равен super. Результат сохранить в переменную res и распечатать
s = "I am super hero!"
print(s[5:10])