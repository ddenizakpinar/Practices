# https://www.hackerrank.com/challenges/a-very-big-sum/problem
# 26.07.2020


def aVeryBigSum(ar):
    return sum(ar)

ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
print(aVeryBigSum(ar))


