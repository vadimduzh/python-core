# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и находит второе
# наибольшее число в этом списке.
#
# Убедитесь, что для ввода: 10 20 4 45 99 результатом будет 45.
numbers_str = input("Enter the list of numbers: ")

str_num_lst = numbers_str.split()
print(str_num_lst)

max_num = int(str_num_lst[0])
second_max_num = int(str_num_lst[0])

for str_num in str_num_lst:
    int_value = int(str_num)
    if int_value > max_num:
        max_num = int_value
for second_str_num in str_num_lst:
    second_int_value = int(second_str_num)
    if second_int_value > second_max_num and second_int_value < max_num:
        second_max_num = second_int_value

print(second_max_num)
