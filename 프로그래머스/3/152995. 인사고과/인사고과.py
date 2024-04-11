# 인센티브를 받지 못할 조건
# 만약 어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우

# 인센티브 지급 조건
# 두 점수의 합이 높은 순으로 석차를 내어 석차에 따라 인센티브가 차등 지급
# scores[0] = 완호 => return 석차 => 해야하는 값
def solution(scores):
    answer = 0  # 만족하는 점수의 수를 저장할 변수 초기화
    wanho = scores[0]  # '완호'의 점수를 첫 번째 요소로 설정
    scores.sort(key=lambda x: (-x[0], x[1]))  # 점수를 첫 번째 요소는 내림차순, 두 번째 요소는 오름차순으로 정렬

    max_score1 = 0  # 두 번째 점수 요소 중 최대값을 추적하기 위한 변수 초기화
    for score in scores:  # 정렬된 점수 목록을 순회
        if score[0] > wanho[0] and score[1] > wanho[1]:  # 현재 점수가 '완호'의 두 점수보다 모두 크면 -1 반환
            return -1

        if score[1] >= max_score1:  # 현재 점수의 두 번째 요소가 지금까지의 최대값보다 크거나 같으면
            max_score1 = score[1]  # 최대값 업데이트
            if sum(score) > sum(wanho):  # 현재 점수의 합이 '완호'의 점수 합보다 크면
                answer += 1  # 만족하는 점수의 수 증가
    return answer + 1  # '완호' 자신도 포함해야 하므로 최종 결과에 1을 더해 반환