def main() :
    N = int(input())
    matrix = []
    for _ in range(N) :
        r, c = map(int, input().split())
        matrix.append((r, c))

    dp = [[(1<<32)] * N for _ in range(N)]

    for i in range(N) :
        dp[i][i] = 0

    for diagonal in range(1, N) :
        for i in range(N - diagonal) :  # 대각선의 우측 한 칸씩
            j = i + diagonal     # 현재 대각선에서 몇 번째 원소인지

            # 각 부분 행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
            for k in range(i, j) :  # k값으로 최적분할 찾기
                dp[i][j] = min(dp[i][j],
                               dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

    
    print(dp[0][N-1])

main()