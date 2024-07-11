# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и подсчитывает количество
# положительных и отрицательных чисел в этом списке.
# Убедитесь, что для ввода: -1 2 -3 4 -5 будет распечатан результат 2 и 3

numbers_str = input("Enter the list of numbers: ")
positive_num = 0
negative_num = 0

str_num_lst = numbers_str.split()
print(str_num_lst)

for str_num in str_num_lst:
    int_value = int(str_num)
    if int_value > 0:
        positive_num = positive_num + 1
    elif int_value < 0:
        negative_num = negative_num + 1

print(positive_num, negative_num)