from collections import deque

# 1000m 이동 가능
# 좌표 형태로 저장 -> lst
# lst = (1000,0) (1000, 1000) N = 2
# ci, cj 기준으로 n개의 편의점 이동 가능 확인
# v[] N = 2

# 조건
# for i (N)
# if v[i] == 0 : ## 미방문
# 범위 내, |cj - nj| + |ci - ni|
# Q 삽입, v[] 표시
def bfs(sj, si, ej, ei) :
    # Q 생성, 필요 변수 등 생성
    q = deque()
    v = [0] * N

    # Q에 초기데이터 삽입, si, sj는 v에 표시X
    q.append((sj, si))

    while q :
        cj, ci = q.popleft()

        if abs(cj - ej) + abs(ci - ei) <= 1000 :    # 목적지까지 도달 가능
            return 'happy'

        # 미방문 모든 편의점 좌표 : 범위 내인지 체크
        for i in range(N) :
            if v[i] == 0 :  # 미방문 편의점
                nj, ni = lst[i]
                if abs(cj-nj) + abs(ci-ni) <= 1000 :    # 범위 내
                    q.append((nj, ni))
                    v[i] = 1
    return 'sad'

T = int(input())
for _ in range(T) :
    N = int(input())
    sj, si = map(int, input().split())
    lst = []
    for _ in range(N) :
        tj, ti = map(int, input().split())
        lst.append((tj, ti))
    ej, ei = map(int, input().split())

    ans = bfs(sj, si, ej, ei)
    print(ans)
