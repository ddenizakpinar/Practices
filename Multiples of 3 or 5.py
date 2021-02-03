# https://www.codewars.com/kata/514b92a657cdc65150000006/

def solution(number):
    ans = 0
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            ans += i
        elif i % 3 == 0:
            ans += i
        elif i % 5 == 0:
            ans += i
    return ans

solution(10)
