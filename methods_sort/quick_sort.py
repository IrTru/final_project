
# метод  - Быстрая сортировка (Quick Sort)
def quick_sort(list_int):

    # сортируем данным методом
    # если длина списка менее двух,
    # то он является отсортированным
    if len(list_int) < 2:
        return list_int
    else:
        # Опорный элемент
        pivot = list_int[0]
        # подсписок элементов меньше опорного
        less = [i for i in list_int[1:] if i < pivot]
        # подсписок элементов больше опорного
        greater = [i for i in list_int[1:] if i > pivot]
        
    return quick_sort(less) + [pivot] + quick_sort(greater)
