# https://www.hackerrank.com/challenges/utopian-tree/problem
# 31.07.2020


def utopianTree(n):
    ans = 1
    for i in range(n):
        if i % 2 == 1:
            ans += 1
        else:
            ans *= 2
    return ans

t = int(input())
for t_itr in range(t):
    n = int(input())
    print(utopianTree(n))