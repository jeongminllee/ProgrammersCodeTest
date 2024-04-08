import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
for m in range(M) :
    i, j = map(int, input().split())
    print(sum(lst[i-1:j]))