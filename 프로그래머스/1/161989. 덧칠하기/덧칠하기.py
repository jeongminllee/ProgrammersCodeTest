def solution(n, m, section):
    # 페인트칠 해야 할 횟수
    answer = 0
    # 시작 순서 설정
    i = 0
    while i < len(section) :
        # 시작 구역 설정
        s = section[i]
        # 롤러로 칠할 수 있는 구역 설정
        e = s + m - 1
        # 현재 구역부터 롤러로 칠할 수 있는 범위 내의 다음 구역들을 확인
        while i < len(section) and section[i] <= e :
            i += 1
        # 페인트칠 횟수 증가
        answer += 1
    return answer