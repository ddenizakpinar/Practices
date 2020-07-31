# https://www.hackerrank.com/challenges/angry-professor/problem
# 31.07.2020


def angryProfessor(k, a):
    result = [x for x in a if x < 1]
    if len(result) < k:
        return "YES"
    return "NO"

t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    print(angryProfessor(k, a))