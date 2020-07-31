# https://www.hackerrank.com/challenges/bon-appetit/problem
# 31.07.2020


def bonAppetit(bill, k, b):
    if (sum(bill) - bill[k]) // 2 == b:
        print('Bon Appetit')
        return
    else:
        print(bill[k] // 2)

nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
bonAppetit(bill, k, b)