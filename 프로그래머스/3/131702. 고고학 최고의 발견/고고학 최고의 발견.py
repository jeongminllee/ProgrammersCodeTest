import copy

# 상하좌우 및 현재 위치에 대한 변화량
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

# 특정 위치의 시계와 인접한 시계를 회전시키는 함수
def rotate(x, y, lst, rt):
    n = len(lst)  # 시계 배열의 크기
    for k in range(5):  # 현재 위치 및 상하좌우 위치에 대해 반복
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:  # 유효한 위치인지 확인
            lst[ny][nx] = (lst[ny][nx] + rt) % 4  # 시계를 rt만큼 회전

# 최소 회전 횟수를 찾는 함수
def solution(clockHands):
    answer = float('inf')  # 최소 회전 횟수를 저장할 변수, 초기값은 무한대
    n = len(clockHands)  # 시계 배열의 크기

    # 첫 번째 열에 대해 가능한 모든 회전 조합을 시도
    for i in range(4 ** n):
        tmp = 0  # 현재 조합에 대한 회전 횟수
        tmp_clock = copy.deepcopy(clockHands)  # 시계 배열의 복사본 생성
        for j in range(n):  # 첫 번째 열에 대해 반복
            rt = i % 4 ** (j + 1) // 4 ** j  # j번째 시계의 회전 횟수 계산
            if rt == 0:
                continue

            rotate(j, 0, tmp_clock, rt)  # j번째 시계와 인접한 시계들 회전
            tmp += rt  # 회전 횟수 추가

        # 두 번째 열부터 마지막 열까지 현재 조건을 만족하는지 확인하며 회전
        for y in range(1, n):
            for x in range(n):
                if tmp_clock[y - 1][x] == 0:  # 이전 열의 시계가 12시를 가리키면 패스
                    continue
                rt = 4 - tmp_clock[y - 1][x]  # 필요한 회전 횟수 계산
                rotate(x, y, tmp_clock, rt)  # 회전
                tmp += rt  # 회전 횟수 추가

        # 마지막 행이 모두 12시를 가리키는지 확인
        if sum(tmp_clock[-1]) == 0:
            answer = min(answer, tmp)  # 최소 회전 횟수 업데이트

    return answer  # 최소 회전 횟수 반환
