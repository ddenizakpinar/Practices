# https://www.hackerrank.com/challenges/strong-password/problem
# 14.03.2020


#!/bin/python3

import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    
    number, lower, upper, special = True, True, True, True
    
    for letter in password:
        if letter in numbers:
            number = False
        if letter in lower_case:
            lower = False
        if letter in upper_case:
            upper = False
        if letter in special_characters:
            special = False
    
    errors = number + lower + upper + special
    
    return errors if n >= 6 else max(6 - n, errors)
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)

