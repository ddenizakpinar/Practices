# https://www.hackerrank.com/challenges/funny-string/problem
# 20.03.2020

#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):
    rs = s[::-1]
    for i in range(0, len(s)-1):
        print(s[i])
        if abs(ord(s[i]) - ord(s[i+1])) !=  abs(ord(rs[i]) - ord(rs[i+1])):
            return "Not Funny"
    return "Funny"
            

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

    print(result)

