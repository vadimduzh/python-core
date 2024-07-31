def simple_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                value = lst[i]
                lst[i] = lst[j]
                lst[j] = value
    return lst


res = simple_sort([1, 3, 2, 14, 6, 12, 4, 22, 0])
print(res)
