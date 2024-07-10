# Напишите программу, которая запрашивает у пользователя целое неотрицательное число N и вычисляет его факториал.
# Факториал числа N (обозначается как N!) — это произведение всех целых чисел от 1 до N. Если N = 0, то факториал
# числа 0 равен 1.
# Факториал числа N = 5 считается как  5 * 4 * 3 * 2 * 1 и равен 120.
#
# Подсказка: можно использовать цикл for и диапазон range.
num = int(input("Enter the number >= 0: "))
factorial = 1

if num > 0:
    for N in range(1, num + 1):
        factorial = factorial * N
    print("N!:", factorial)
else:
    print("N!:", 1)