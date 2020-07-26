# https://www.hackerrank.com/challenges/staircase/problem
# 26.07.2020


def staircase(n):
    for i in range(1,n+1):
        print((" " * (n-i)) + (i*"#"))

n = int(input())
print(staircase(n))


