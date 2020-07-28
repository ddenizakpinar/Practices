# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# 28.07.2020


def breakingRecords(scores):
    minCounter, maxCounter = 0,0
    minimum,maximum = scores[0],scores[0]
    for score in scores:
        if minimum != min(minimum,score):
            minCounter+=1
            minimum = min(minimum,score)
        if maximum != max(maximum,score):
            maxCounter+=1
            maximum = max(maximum,score)
    return maxCounter,minCounter

n = int(input())
scores = list(map(int, input().rstrip().split()))
print(breakingRecords(scores))