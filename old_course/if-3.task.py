# - Пользователь вводит 3 числа и сохраняет в переменных a, b и c (не забудь про int())
# - Если a = b и a = c, тогда на экран выводим текст Все числа равны
# - Иначе выводим 3 числа не совпадают.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the lsat number: "))

if a == b and a == c:
    print("All number are equal")
else:
    print("All numbers dont match")

