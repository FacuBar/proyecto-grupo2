from algo1 import Array
from hashmap import HashMapNode


def mergeSort(arr):
    divide(arr, 0, len(arr) - 1)


def divide(arr, start, tail):
    if start < tail:
        med = (start + tail)//2

        divide(arr, start, med)
        divide(arr, med + 1, tail)

        merge(arr, start, med, tail)


def merge(arr, start, med, tail):
    l1, l2 = (med-start+1), (tail-med)
    left = Array(l1, HashMapNode())
    right = Array(l2, HashMapNode())

    for i in range(l1):
        left[i] = arr[start + i]
    for j in range(l2):
        right[j] = arr[med + 1 + j]

    i = j = 0
    k = start
    while i < l1 and j < l2:
        if left[i].value >= right[j].value:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < l1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < l2:
        arr[k] = right[j]
        j += 1
        k += 1
