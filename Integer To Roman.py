# https://leetcode.com/problems/integer-to-roman


def intToRoman(num):
    dict = {
        'M':1000,
        'CM':900,
        'D':500,
        'CD':400,
        'C':100,
        'XC':90,
        'L':50,
        'XL':40,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'III':3,
        'II':2,         
        'I':1
    }
    ans = ''
    while num > 0:
        for key in dict:
            if dict[key] <= num:
                rep = num // dict[key]
                num -= dict[key] * rep
                ans += key * rep
    return ans

s = int(input())
print(intToRoman(s))