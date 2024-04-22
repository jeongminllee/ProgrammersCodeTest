def solution(priorities, location):
    answer = 0  # 출력된 문서의 수를 카운트
    # priorities의 각 요소와 그 인덱스를 튜플로 묶어 queue 리스트 생성
    queue = [(i, q) for i, q in enumerate(priorities)]

    while True:
        pri = queue.pop(0)  # 맨 앞의 문서를 대기열에서 제거
        # 대기열에 pri보다 우선순위가 높은 문서가 존재하는지 확인
        if any(pri[1] < q[1] for q in queue):
            queue.append(pri)  # 우선순위가 더 높은 문서가 있으면 맨 뒤로 이동
        else:
            answer += 1  # 그렇지 않으면 문서를 출력하고 카운트 증가
            # 현재 출력된 문서가 사용자가 알고 싶어하는 문서의 위치와 일치하는지 확인
            if pri[0] == location:
                return answer  # 일치하면 현재까지 출력된 문서의 수를 반환하고 함수 종료
