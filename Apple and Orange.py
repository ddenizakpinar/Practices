# https://www.hackerrank.com/challenges/apple-and-orange/problem
# 28.07.2020


def countApplesAndOranges(s, t, a, b, apples, oranges):
    ansApple, ansOrange = 0,0
    for i in apples:
        if a + i >= s and a + i <= t:
            ansApple += 1
    for i in oranges:
        if b + i <= t and b + i >= s:
            ansOrange += 1
    print(ansApple)
    print(ansOrange)


st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)