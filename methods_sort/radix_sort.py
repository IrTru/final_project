
# метод  - Поразрядная сортировка (Radix Sort)
def radix_sort(list_int):

    # находим длину самого длинного числа
    max_digit = max([len(str(num)) for num in list_int])
    # система счисления
    radix = 10
    # создаем промежуточные списки
    lists = [[] for i in range(radix)]
    # перебираем все разряды, начиная с нулевого
    for i in range(0, max_digit):
        # пересобираем все элементы в списке
        for elem in list_int:
            # перебираем цифру текушего разряда, для каждого числа
            digit = (elem // radix ** i) % radix
            # добавляем число в промежуточный массив
            lists[digit].append(elem)
        # собираем в исходный список ненулевые значения
        list_int = [x for queue in lists for x in queue]
        # очищаем промежуточный список
        lists = [[] for i in range(radix)]
        
    return list_int


