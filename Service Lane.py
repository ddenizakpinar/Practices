# https://www.hackerrank.com/challenges/service-lane/problem
# 01.08.2020


def serviceLane(n, width, cases):
    return [min(width[i[0]:i[1]+1]) for i in cases]

nt = input().split()
n = int(nt[0])
t = int(nt[1])
width = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))
print(serviceLane(n, width, cases))