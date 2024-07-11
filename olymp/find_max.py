# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и находит
# наибольшее число в этом списке.
#
# Подсказка: см. count_even_odd.py - там есть как разобрать строку.
numbers_str = input("Enter the list of numbers: ")

str_num_lst = numbers_str.split()
print(str_num_lst)

max_num = int(str_num_lst[0])

for str_num in str_num_lst:
    int_value = int(str_num)
    if int_value > max_num:
        max_num = int_value

print(max_num)
