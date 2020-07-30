# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# 30.07.2020


def designerPdfViewer(h, word):
    highest = 0
    for letter in word:
        highest = max(h[ord(letter)-97],highest)
    return len(word) * highest

h = list(map(int, input().rstrip().split()))
word = input()
print(designerPdfViewer(h, word)) 