# - Пользователь вводит 2 числа и сохраняет в переменных a и b (не забудь про int())
# - Если a = b, тогда на экран выводим текст a равно b
# - Если a < b, тогда на экран выводим текст a меньше b
# - иначе выдоим a больше b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a == b:
    print("a = b")
elif a < b:
    print("a меньше b")
else:
    print("a больше b")
