# https://www.hackerrank.com/challenges/repeated-string/problem
# 09.08.2020


def chocolateFeast(n, c, m):
    wrapper = n // c
    ans = wrapper
    while wrapper >= m:
        wrapper -= m-1
        ans += 1
    return ans

t = int(input())
for t_itr in range(t):
    ncm = input().split()
    n = int(ncm[0])
    c = int(ncm[1])
    m = int(ncm[2])
    print(chocolateFeast(n, c, m))