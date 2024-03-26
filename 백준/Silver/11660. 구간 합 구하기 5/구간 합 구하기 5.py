N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sm = [[0] * (N + 1) for _ in range(N + 1)]
for a in range(1, N + 1) :
    for b in range(1, N + 1):
        sm[a][b] = sm[a - 1][b] + sm[a][b - 1] - sm[a - 1][b - 1] + arr[a - 1][b - 1]

for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    ans = sm[x2][y2] - sm[x1 - 1][y2] - sm[x2][y1 - 1] + sm[x1 - 1][y1 - 1]
    print(str(ans))