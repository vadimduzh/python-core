# - Пользователь вводит 2 числа и сохраняет в переменных a и b (не забудь про int())
# - Если a равно b, тогда на экран выводим текст a равно b, иначе выдоим a не равно b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a == b:
    print("a ровно b")
else:
    print("a не ровно b")
