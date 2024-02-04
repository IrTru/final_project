
# метод - Сортировка подсчетом (Counting Sort)
def counting_sort(list_int):

    largest = max(list_int)
    count = [0]*(largest+1)
    for i in range(len(list_int)):
        count[list_int[i]] = count[list_int[i]]+1
    count[0] = count[0]-1

    for i in range(1, largest+1):
        count[i] = count[i] + count[i-1]
    
    result=[None]*len(list_int)
    for x in reversed(list_int):
        result[count[x]] = x
        count[x] = count[x]-1

    return result
