import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]

M = int(input())
for i in range(N) :
    dp[i][i] = 1

for mid in range(N) :
    for l in range(1, N) :
        if 0 <= mid - l and mid + l < N and lst[mid-l] == lst[mid+l] and dp[mid-l+1][mid+l-1] :
            dp[mid-l][mid+l] = 1
        else :
            break
            
for i in range(N - 1) :
    if lst[i] == lst[i+1] :
        dp[i][i+1] = 1

for i in range(N - 1) :
    ii = i + 1
    for l in range(1, N) :
        if 0 <= i - l and ii + l < N and lst[i-l] == lst[ii+l] and dp[i-l+1][ii+l-1] :
            dp[i-l][ii+l] = 1
        else :
            break

for _ in range(M) :
    S, E = map(int, input().split())

    print(dp[S-1][E-1])