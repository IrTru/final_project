
# функция преобразования в двоичную кучу, где list_int список,i - корневой индекс и n размер кучи (для Heap Sort)
def heapify(list_int, n, i):
    
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and list_int[i] < list_int[left]:
        # проверка существования левого элемента, который больше корня
        largest = left
    if right < n and list_int[largest] < list_int[right]:
        # проверка существования правого элемента, который больше корня
        largest = right
    if largest != i:
        # меняем корень, если того требуется
        list_int[i], list_int[largest] = list_int[largest], list_int[i]
        # применяем функцию к корневому элементу
        heapify(list_int, n, largest)

# метод - Пирамидальная сортировка (Heap Sort)
def heap_sort(list_int):

    # сортируем данным методом
    n = len(list_int)
    for i in range(n, -1, -1):
        heapify(list_int, n, i)
    for i in range(n-1, 0, -1):
        # меняем элементы местами
        list_int[i], list_int[0] = list_int[0], list_int[i]
        heapify(list_int, i, 0)
