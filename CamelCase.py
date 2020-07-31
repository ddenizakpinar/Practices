# https://www.hackerrank.com/challenges/camelcase/problem
# 31.07.2020


def camelcase(s):
    ans = 1
    for i in s:
        if i.isupper():
            ans += 1
    return ans

s = input()
print(camelcase(s))