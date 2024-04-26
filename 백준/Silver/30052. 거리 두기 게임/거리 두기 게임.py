n, m = map(int, input().split())
d = int(input())
ans = 0
arr = [[0] * (m + 1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,m+1) :
        if abs(1 - i) + abs(1 - j) < d:
            arr[i][j] = 1

        if abs(n - i) + abs(1 - j) < d and arr[i][j] == 1:
            arr[i][j] = 2

        if abs(1 - i) + abs(m - j) < d and arr[i][j] == 2:
            arr[i][j] = 3

        if abs(n - i) + abs(m - j) < d and arr[i][j] == 3:
            ans += 1

print(ans)