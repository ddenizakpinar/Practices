# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/

def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count


print(persistence(39))
