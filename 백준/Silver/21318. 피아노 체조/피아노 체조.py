import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))
Q = int(input())

sm = [0] * (N + 1)
for i in range(1, N + 1) :
    if lst[i - 1] > lst[i]:
        sm[i] = sm[i - 1] + 1
    else :
        sm[i] = sm[i - 1]

for _ in range(Q) :
    x, y = map(int, input().split())
    print(sm[y] - sm[x])