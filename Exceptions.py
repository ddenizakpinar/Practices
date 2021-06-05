# https://www.hackerrank.com/challenges/exceptions/problem

count = int(input())

for _ in range(count):
    a, b = input().split()

    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")
