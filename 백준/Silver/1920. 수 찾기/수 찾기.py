import sys
input = sys.stdin.readline

N = int(input())
a = set(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

for j in b :
    if j in a :
        print(1)
    else :
        print(0)