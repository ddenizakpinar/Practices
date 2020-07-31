# https://www.hackerrank.com/challenges/minimum-distances/problem
# 01.08.2020


def minimumDistances(a):
    ans = 100000
    for i in a:
        if a.count(i) > 1:
            first = a.index(i)
            second = a.index(i, first+1)
            ans = min(second - first, ans)
    return ans if ans != 100000 else -1

n = int(input())
a = list(map(int, input().rstrip().split()))
print(minimumDistances(a))