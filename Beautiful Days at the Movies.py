# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# 31.07.2020


def beautifulDays(i, j, k):
    ans = 0 
    for i in range(i,j+1):
        if (int(str(i)[::-1]) - i) % k == 0:
            ans += 1
    return ans

ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])
print(beautifulDays(i, j, k))
