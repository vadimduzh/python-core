# Напишите программу, которая запрашивает у пользователя список чисел, разделенных пробелами, и вычисляет их
# среднее арифметическое.
# Убедиться, что 1 2 3 4 5 среднее арифметическое: 3.0
numbers_str = input("Enter the list of numbers: ")

str_num_lst = numbers_str.split()
print(str_num_lst)

sum = 0
for str_num in str_num_lst:
    int_value = int(str_num)
    sum = sum + int_value

average_value = sum / len(str_num_lst)
print(average_value)

