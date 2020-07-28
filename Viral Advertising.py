# https://www.hackerrank.com/challenges/strange-advertising/problem
# 28.07.2020



def viralAdvertising(n):
    ans ,shared = 0, 5
    ans += shared // 2

    for _ in range(n-1):
        shared = (shared // 2) * 3
        ans += shared // 2
        
    return ans


n = int(input())
print(viralAdvertising(n))
