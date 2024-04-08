import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))
M = int(input())
sumlst = [0] * (N + 1)

for i in range(1, N+1) :
    sumlst[i] = sumlst[i-1] + lst[i]

for _ in range(M) :
    i, j = map(int, input().split())
    print(sumlst[j] - sumlst[i-1])