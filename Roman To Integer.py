# https://leetcode.com/problems/roman-to-integer/


def romanToInt(s):
    dict = {
        'CM':900,
        'M':1000,
        'CD':400,
        'D':500,
        'XC':90,
        'C':100,
        'XL':40,
        'L':50,
        'IX':9,
        'X':10,
        'IV':4,
        'V':5,
        'III':3,
        'II':2,         
        'I':1
    }
    ans = 0
    while s:
        for key in dict:
            if key in s:
                s = s.replace(key,'',1)
                ans += dict[key]
    return ans

s = input()
print(romanToInt(s))