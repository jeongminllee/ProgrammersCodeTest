def solution(target):
    # dp[i][0] = 최소 다트, dp[i][1] = 싱글+불 다트 수
    # 최솟값, 최대값 이기 때문에 큰 수로 시작, 작은 수로 시작
    dp = [[float('inf'), 0] for _ in range(300_000)]

    # 가능한 싱글 점수들
    score_lst = [i for i in range(1, 21)]
    # 시작 지점 초기화
    dp[0][0] = 0

    # target까지 탐색
    for i in range(target) :
        def dart(idx, cnt) :
            # 던진 다트 수를 갱신할 필요가 있는 경우
            if dp[i+idx][0] >= dp[i][0] + 1 :
                if dp[i+idx][0] == dp[i][0] + 1 :
                    # 기존 값과 비교하여 '싱글' 또는 '불'을 맞춘 횟수 갱신
                    dp[i+idx][1] = max(dp[i+idx][1], dp[i][1] + cnt)
                else :
                    # 던진 다트 수와 '싱글' 또는 '불'을 맞춘 횟수를 갱신
                    dp[i+idx] = [dp[i][0]+1, dp[i][1]+cnt]

        for j in score_lst :
            # 싱글, 더블, 트리플을 순서대로 적용하여 갱신
            for mul, hit_cnt in [[1,1],[2,0],[3,0]] :
                dart(j*mul, hit_cnt)

        # "불"에 대해서도 확인하여 갱신
        dart(50, 1)

    # target 까지 도달하는 데 필요한 최소 다트 수와 '싱글' 또는 '불'을 맞춘 횟수 반환
    return dp[target]