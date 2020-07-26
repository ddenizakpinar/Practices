# https://www.hackerrank.com/challenges/simple-array-sum/problem
# # 26.07.2020


def diagonalDifference(arr):
    ltr, rtl = 0,0
    for i in range(len(arr)):
        ltr += arr[i][i]
        rtl += arr[i][-i-1]
    return abs(ltr-rtl)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

print(diagonalDifference(arr))