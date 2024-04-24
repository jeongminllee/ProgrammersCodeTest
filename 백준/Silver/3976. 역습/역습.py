T = int(input())
for _ in range(T) :
    n, l1, l2, s1, s2 = map(int, input().split())   # 점, 수비수가 스트라이커한테 긴패스1, 2, 스트라이커 슛 1, 2
    p1 = list(map(int, input().split()))            # 스트라이커1 => 2 패스 난이도
    d1 = list(map(int, input().split()))            # 스트라이커1 드리블
    p2 = list(map(int, input().split()))            # 스트라이커2 => 1 패스 난이도
    d2 = list(map(int, input().split()))            # 스트라이커2 드리블

    dp = [[0] * 2 for _ in range(n+1)]              # [0] = 1번 루트, [1] = 2번 루트

    # 첫 번째 점에서의 난이도 초기화
    dp[1][0] = l1
    dp[1][1] = l2

    # 각 점에서의 최소 난이도 계산
    for i in range(2, n+1) :
        # l1 => d1 or p2
        dp[i][0] = min(dp[i-1][0] + d1[i-2], dp[i-1][1] + p2[i-2])
        # l2 => d2 or p1
        dp[i][1] = min(dp[i-1][1] + d2[i-2], dp[i-1][0] + p1[i-2])

    ans = min(dp[n][0] + s1, dp[n][1] + s2)
    print(ans)