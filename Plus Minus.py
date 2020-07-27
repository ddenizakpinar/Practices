# https://www.hackerrank.com/challenges/plus-minus/problem
# 27.07.2020


def plusMinus(arr):
    pos,neg,zero = [],[],[]
    
    for i in arr:
        if i > 0:
            pos.append(i)
        if i == 0:
            zero.append(i)
        if i < 0:
            neg.append(i)
            
    print(len(pos)/len(arr))
    print(len(neg)/len(arr))
    print(len(zero)/len(arr))


n = int(input())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)