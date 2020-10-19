# https://leetcode.com/problems/reverse-string


def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    for i in range(int(len(s)/2)):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
    return s
  
s = ["h", "e", "l", "l", "o"]
print(reverseString(s))
