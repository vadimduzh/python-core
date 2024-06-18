# Используя if elif напиши программу, которая запрашивает у пользователя число и выводит, является ли оно положительным,
# отрицательным или равным нулю.
num = int(input("Enter the num: "))
if num > 0:
    print("This is positive num")
elif num == 0:
    print("This is zero")
else:
    print("This is negative num")


# Напиши программу, которая запрашивает у пользователя номер месяца (от 1 до 12) и записывает в переменную season
# соответствующее время года (зима, весна, лето, осень).
# После выхода из if распечатать значение переменной season
season = int(input("Enter the num of the month(from 1 to 12): "))
if season == 1 or season == 12 or season == 2:
    print("This is Winter")
elif season == 3 or season == 4 or season == 5:
    print("This is Spring")
elif season == 6 or season == 7 or season == 8:
    print("This is Summer")
elif season == 9 or season == 10 or season == 11:
    print("This is Fall")
print(season)

# Напиши программу, которая запрашивает у пользователя два целых числа и выводит большее из них.
# Нужно учесть, что два числа могут быть равными.
num1 = int(input("Enter the num: "))
num2 = int(input("Enter the num: "))
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print("They are equal")

# Напиши программу, которая запрашивает у пользователя оценку (от 1 до 5) и выводит сообщение об успеваемости:
# "Превосходно", "Отлично", "Хорошо", "Удовлетворительно", "Неудовлетворительно"
mark = int(input("Enter the mark: "))
if mark == 1:
    print("Неудовлетворительно")
elif mark == 2:
    print("Удовлетворительно")
elif mark == 3:
    print("Хорошо")
elif mark == 4:
    print("Отлично")
elif mark == 5:
    print("Превосходно")

# Напиши программу, которая запрашивает у пользователя число и проверяет, находится ли оно в диапазоне
# от 1 до 100 включительно.
num = int(input("Enter the num: "))
if 1 <= num <= 100:
    print("Число находится в диапазоне от 1 до 100")
else:
    print("Это число не находится в диапазоне от 1 до 100")

# Напиши программу, которая запрашивает у пользователя строку и проверяет, начинается ли она с буквы "а".
# У строки есть метод startswith, который говорит о том, начинается ли строка с указанной строки.
string = input("Введите число, которое начинается с буквы а: ")
if string.startswith("а" ,0):
    print("Строка начинается с буквы а")

# Напиши программу, которая запрашивает у пользователя пароль и проверяет, совпадает ли он с заранее заданным
# значением correct_password.
correct_password = "password123"
password = input("Enter the password: ")
if password == correct_password:
    print("They are equal")
else:
    print("Wrong password")

