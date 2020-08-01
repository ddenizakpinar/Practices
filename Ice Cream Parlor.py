# https://www.hackerrank.com/challenges/icecream-parlor/problem
# 01.08.2020


def icecreamParlor(m, arr):
    dict={}
    for i, val in enumerate(arr):
        dict[val] = i
   
    for i, val in enumerate(arr):
        s = m - val
        if s in dict:
            if dict[s] != i:
                return i+1, dict[s]+1

t = int(input())
for t_itr in range(t):
    m = int(input())
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(icecreamParlor(m, arr))