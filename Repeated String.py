# https://www.hackerrank.com/challenges/repeated-string/problem
# 09.08.2020


def repeatedString(s, n):
    return s.count('a') * (n // len(s)) + s[:n % len(s):].count('a')

s = input()
n = int(input())
print(repeatedString(s, n))