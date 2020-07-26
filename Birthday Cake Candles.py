# https://www.hackerrank.com/challenges/simple-array-sum/problem
# 26.07.2020


def birthdayCakeCandles(ar):
    return ar.count(max(ar))

ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
print(birthdayCakeCandles(ar))
