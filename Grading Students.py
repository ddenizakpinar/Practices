# https://www.hackerrank.com/challenges/grading/problem
# 28.07.2020


def gradingStudents(grades):
    res = []
    for i in grades:
        diff = 5 - i % 5
        if diff < 3 and i >= 38:
            res.append(i+diff)
            continue
        res.append(i)
    return res


grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

print(gradingStudents(grades))