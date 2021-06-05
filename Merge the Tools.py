# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s_list = list(string[i:i+k])
        print("".join(sorted(set(s_list), key=s_list.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)