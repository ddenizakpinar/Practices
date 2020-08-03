# https://www.hackerrank.com/challenges/permutation-equation/problem
# 03.08.2020


def permutationEquation(p):
    ans = []
    for i in range(1,len(p)+1):
        x1 = p.index(i)
        x2 = p.index(x1+1)
        ans.append(x2+1)
    return ans

n = int(input())
p = list(map(int, input().rstrip().split()))
print(permutationEquation(p))