# https://www.hackerrank.com/challenges/making-anagrams/problem
# 07.08.2020


def makingAnagrams(s1, s2):
    for i in s1:
        if i in s2:
            s1 = s1.replace(i, "", 1)
            s2 = s2.replace(i, "", 1)
    return len(s1) + len(s2)

s1 = input()
s2 = input()
print(makingAnagrams(s1, s2))
