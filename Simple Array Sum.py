# https://www.hackerrank.com/challenges/simple-array-sum/problem
# 26.07.2020


def simpleArraySum(ar):
    return sum(ar)


ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
print(simpleArraySum(ar))


