# https://www.hackerrank.com/challenges/time-conversion/problem
# 27.07.2020


def timeConversion(s):
    time = s[:-2].split(":")
    time[0] = int(time[0]) % 12
    if "PM" in s:
        time[0] = int(time[0]) + 12
    else:
        time[0] = "0"+ str(time[0])
    return ":".join(str(i) for i in time)


s = input()
print(timeConversion(s))