# https://www.hackerrank.com/challenges/sock-merchant/problem
# 02.08.2020


def sockMerchant(n, ar):
    ans = 0
    for i in set(ar):
        ans += ar.count(i) // 2
    return ans

n = int(input())
ar = list(map(int, input().rstrip().split()))
print(sockMerchant(n, ar))