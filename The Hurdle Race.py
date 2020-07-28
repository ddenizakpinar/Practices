# https://www.hackerrank.com/challenges/the-hurdle-race/problem
# 28.07.2020

def hurdleRace(k, height):
    highest = max(height)
    ans = highest - k if highest > k else 0
    return ans


nk = input().split()
n = int(nk[0])
k = int(nk[1])
height = list(map(int, input().rstrip().split()))
print(hurdleRace(k, height))