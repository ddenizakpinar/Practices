# https://www.hackerrank.com/challenges/counting-valleys/problem
# 31.07.2020


def countingValleys(n, s):
    ans, level = 0,0
    for i in s:
        if i == 'D':
            level -= 1
        if i == 'U':
            level += 1
            if level == 0:
                ans += 1
    return ans

n = int(input())
s = input()
print(countingValleys(n, s))
