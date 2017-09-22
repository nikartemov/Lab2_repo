def min(arr):
    minimum=arr[0]
    for element in arr:
        if element<minimum:
            minimum=element
    return minimum


def aver(arr):
    counter = 0
    summ = 0
    for elem in arr:
        summ = summ + elem
        counter += 1
    avere = summ/counter
    return avere


arr = [8, 1, 4, 15]
print(min(arr))
print(aver(arr))