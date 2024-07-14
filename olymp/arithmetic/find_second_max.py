# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и находит второе
# наибольшее число в этом списке.
#
# Убедитесь, что для ввода: 10 20 4 45 99 результатом будет 45.
numbers_str = input("Enter the list of numbers: ")

str_num_lst = numbers_str.split()
print(str_num_lst)

max_1 = int(str_num_lst[0])
for str_num in str_num_lst:
    int_value = int(str_num)

    if int_value > max_1:
        max_1 = int_value

max_2 = None
for str_num in str_num_lst:
    int_value = int(str_num)

    if int_value == max_1:
        continue

    if max_2 is None or max_2 < int_value:
        max_2 = int_value

print(max_2)

