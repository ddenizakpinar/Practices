# https://www.hackerrank.com/challenges/insertionsort1/problem
# 01.08.2020


def insertionSort1(n, arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                print(*arr)
        arr[j+1] = key 
    print(*arr)

n = int(input())
arr = list(map(int, input().rstrip().split()))
insertionSort1(n, arr)