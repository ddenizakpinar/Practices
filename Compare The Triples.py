# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# 27.07.2020


def compareTriplets(a, b):
    alice, bob = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice = alice + 1
        elif a[i] < b[i]:
            bob = bob + 1
    return [alice,bob]


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
print(compareTriplets(a, b))