# https://www.hackerrank.com/challenges/find-digits/problem
# 01.08.2020


def findDigits(n):
    ans = 0
    for i in str(n):
        if i != '0' and n % int(i) == 0:
            ans += 1
    return ans

t = int(input())
for t_itr in range(t):
    n = int(input())
    print(findDigits(n))