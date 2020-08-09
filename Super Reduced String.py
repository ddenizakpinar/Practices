# https://www.hackerrank.com/challenges/repeated-string/problem
# 09.08.2020


def superReducedString(s):
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
    if s == "":
        return "Empty String"
    return s

s = input()
print(superReducedString(s))
