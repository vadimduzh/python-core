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
if 0 < season < 4:
    print("This is Winter")
elif 3 < season < 7:
    print("This is Spring")
elif 6 < season < 10:
    print("This is Summer")
elif 9 < season <= 12:
    print("This is Fall")

# Напиши программу, которая запрашивает у пользователя два целых числа и выводит большее из них.
# Нужно учесть, что два числа могут быть равными.

# Напиши программу, которая запрашивает у пользователя оценку (от 1 до 5) и выводит сообщение об успеваемости:
# "Отлично", "Хорошо", "Удовлетворительно", "Неудовлетворительно".


# Напиши программу, которая запрашивает у пользователя число и проверяет, находится ли оно в диапазоне
# от 1 до 100 включительно.

# Напиши программу, которая запрашивает у пользователя строку и проверяет, начинается ли она с буквы "а".
# У строки есть метод startswith, который говорит о том, начинается ли строка с указанной строки.

# Напиши программу, которая запрашивает у пользователя пароль и проверяет, совпадает ли он с заранее заданным
# значением correct_password.
correct_password = "password123"
