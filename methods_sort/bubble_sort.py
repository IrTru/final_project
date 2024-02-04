
# метод - Сортировка пузырьком (Bubble Sort)
def bubble_sort(list_int):

    # выполняем метод сортировки
    last_elem_index = len(list_int)-1 
    # проходим по каждому элементу списка
    for elem in range(last_elem_index, 0, -1):
        for idx in range(elem):
            # выполняем сравнение
            if list_int[idx] > list_int[idx+1]:
                list_int[idx], list_int[idx+1] = list_int[idx+1], list_int[idx]

    return list_int
