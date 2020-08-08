#  https://www.hackerrank.com/challenges/game-of-thrones/problem
# 08.08.2020


def gameOfThrones(s):
    freq = {}
    middle = True
    for i in range(ord('a'), ord('z')+1):
        freq[chr(i)] = 0
    
    for c in s:
        freq[c] += 1

    for i in freq:
        if freq[i] % 2 != 0:
            if middle == True:
                middle = False
                continue
            else:
                return "NO" 
    return "YES"

s = input()
print(gameOfThrones(s))