# https://www.hackerrank.com/challenges/quicksort1/problem
# 08.08.2020


def quickSort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)
    return arr

def partition(arr,low,high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] =  arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(quickSort(arr, 0, len(arr)-1))