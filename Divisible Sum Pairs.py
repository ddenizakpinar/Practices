# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# 28.07.2020


def divisibleSumPairs(n, k, ar):
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i] + ar[j]) % k == 0:
                ans += 1
    return ans

nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
print(divisibleSumPairs(n, k, ar))