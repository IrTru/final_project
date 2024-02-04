
# метод  - Сортировка слиянием (Merge Sort)
def merge_sort(list_int):

    # сортируем данным методом
    if len(list_int) > 1:
        # делим список пополам
        mid = len(list_int) // 2
        left = list_int[:mid]
        right = list_int[mid:]
        # применяем функцию к левой и правой частям
        merge_sort(left)
        merge_sort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list_int[c] = left[a]
                a += 1
            else:
                list_int[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            list_int[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            list_int[c] = right[b]
            b += 1
            c += 1

    return list_int