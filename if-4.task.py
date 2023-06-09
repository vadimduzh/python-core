# - Пользователь вводит 3 числа и сохраняет в переменных a, b и c (не забудь про int())
# - Если a = c или b = c, тогда на экран выводим текст Есть совпадение
# - Иначе выводим Нет совпадения!

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the lsat number: "))

if a == b or a == c:
    print("Есть совпадение")
else:
    print("Нет совпадения")
