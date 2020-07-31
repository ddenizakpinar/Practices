# https://www.hackerrank.com/challenges/picking-numbers/problem
# 31.07.2020


def pickingNumbers(a):
    ans = 0
    
    for i in a:
        m = a.count(i)
        n = a.count(i-1)
        m += n
        ans = max(m, ans)
    return ans

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
print(pickingNumbers(a))