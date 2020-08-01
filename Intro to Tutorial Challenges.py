# https://www.hackerrank.com/challenges/tutorial-intro/problem
# 01.08.2020


def introTutorial(V, arr):
    return arr.index(V)

V = int(input())
n = int(input())
arr = list(map(int, input().rstrip().split()))
print(introTutorial(V, arr))