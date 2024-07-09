# В файле data/olymp-003-in.txt заданы числа.
# Нужно сложить все числа и результат записать в файл tmp/olymp-003-out.txt

# Подсказка
# - заводим переменную со значением 0, в которой будет храниться результат
# - читаем каждую строку из файла (используем for - см. file-1.task.py в конце)
# - переводим прочитанную строку в число и добавляем к результ

file = open("../data/olymp-003-in.txt", "r")

s1 = file.readline()
num1 = int(s1)

s2 = file.readline()
num2 = int(s2)

s3 = file.readline()
num3 = int(s3)

result = num1 + num2 + num3
res = str(result)

file.close()

file = open("../tmp/olymp-003-out.txt", "w")

file.write(res)

file.close()
