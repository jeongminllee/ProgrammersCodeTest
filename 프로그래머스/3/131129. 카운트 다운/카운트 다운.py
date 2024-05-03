def solution(target):
    # 점수 업데이트를 위한 내부 함수 정의
    # score: 더할 점수, single: 싱글 점수 여부 (싱글일 때만 두 번째 요소 증가)
    def update_dp(score, single=True):
        # target 점수까지 반복
        for n in range(target + 1):
            next_score = n + score  # 다음 점수 계산
            if next_score > target:  # 목표 점수를 초과하는 경우 루프 중단
                break
            # dp 배열 업데이트 조건 확인 및 업데이트
            if dp[next_score][0] > dp[n][0] + 1 or \
                    (dp[next_score][0] == dp[n][0] + 1 and dp[next_score][1] < dp[n][1] + single):
                dp[next_score] = [dp[n][0] + 1, dp[n][1] + single]

    # dp 배열 초기화 (무한대로 설정하여 최소값 찾기 용이하게 함)
    dp = [[float('inf'), -1] for _ in range(target + 1)]
    dp[0] = [0, 0]  # 0점일 때의 기본값 설정

    # 1점부터 20점까지 반복하여 싱글, 더블, 트리플 점수 업데이트
    for i in range(1, 21):
        update_dp(i)  # 싱글
        update_dp(i * 2, False)  # 더블 (싱글이 아니므로 두 번째 요소 증가 안 함)
        update_dp(i * 3, False)  # 트리플 (싱글이 아니므로 두 번째 요소 증가 안 함)

    update_dp(50)  # 불 (50점)

    return dp[target]  # 목표 점수에 해당하는 dp 배열의 값을 반환