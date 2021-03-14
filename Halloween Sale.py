# https://www.hackerrank.com/challenges/halloween-sale/problem
# 14.03.2020


#!/bin/python3

import math
import os
import random
import re
import sys

def howManyGames(p, d, m, s):
    ans = 0
    while (s >= p):
        ans += 1
        s = s - p
        p = p - d if p - d >= m else m
    return ans


if __name__ == '__main__':

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)
    print(answer)
