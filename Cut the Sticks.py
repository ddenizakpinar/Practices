# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# 06.08.2020


def cutTheSticks(arr, ans):
    if len(arr) == 0:
        return ans
    ans.append(len(arr))
    arr = [x for x in arr if x != min(arr)]
    return cutTheSticks(arr, ans)

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(cutTheSticks(arr, []))