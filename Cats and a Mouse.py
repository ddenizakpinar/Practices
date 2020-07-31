# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
# 30.07.2020


def catAndMouse(x, y, z):
    if abs(x-z) < abs(y-z):
        return "Cat A"
    elif abs(y-z) < abs(x-z):
        return "Cat B" 
    return "Mouse C"

q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    print(catAndMouse(x, y, z))