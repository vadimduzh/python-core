# В файле data/olymp-004-in.txt заданы числа.
# Нужно перемножить все числа и результат записать в файл tmp/olymp-004-out.txt

file = open("data/olymp-004-in.txt", "r")

s1 = file.readline()
num1 = int(s1)

s2 = file.readline()
num2 = int(s2)

s3 = file.readline()
num3 = int(s3)

result = num1 * num2 * num3
res = str(result)

file.close()

file = open("tmp/olymp-004-out.txt", "w")

file.write(res)

file.close()

