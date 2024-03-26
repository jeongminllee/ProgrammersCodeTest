N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 누적합 배열 초기화
sm = [[0] * (M + 1) for _ in range(N + 1)]

# 누적합 계산
# [1] sm[0][b] = 0 모든 b에 대해
# [2] sm[a][0] = 0 모든 a에 대해
# [3] sm[a][b] = sm[a-1][b] + sm[a][b-1] - sm[a-1][b-1] + arr[a][b]
for a in range(1, N + 1) :
    for b in range(1, M + 1) :
        sm[a][b] = sm[a-1][b] + sm[a][b-1] - sm[a-1][b-1] + arr[a-1][b-1]

# 쿼리 처리
# 구간합 = sm[x][y] - sm[i-1][y] - sm[x][j-1] + sm[i-1][j-1]
K = int(input())
for _ in range(K) :
    i, j, x, y = map(int, input().split())
    ans = sm[x][y] - sm[i-1][y] - sm[x][j-1] + sm[i-1][j-1]
    print(ans)