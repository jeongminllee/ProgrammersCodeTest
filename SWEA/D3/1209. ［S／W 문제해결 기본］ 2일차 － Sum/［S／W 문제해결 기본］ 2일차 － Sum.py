T = 10

for test_case in range(1, T + 1) :
    _ = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = s3 = s4 = 0
    for i in range(N) :
        s1 = s2 = 0
        for j in range(N) :
            s1 += arr[i][j]
            s2 += arr[j][i]

        ans = max(ans, s1, s2)

        s3 += arr[i][i]
        s4 += arr[i][N-1-i]

    ans = max(ans, s3, s4)
    print(f"#{test_case} {ans}")