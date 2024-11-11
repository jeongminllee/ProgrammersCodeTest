from collections import deque

def bfs(s, e) :
    if s >= e :     # 시작값이 목표값보다 크면 도달 불가능
        return -1

    q = deque()     # deque 생성

    q.append((s, 1))    # 현재값, 연산횟수 튜플로 저장
    v = {s}             # 방문한 숫자 set으로 관리

    while q :
        curr, cnt = q.popleft()
        
        # 두 가지 연산 시도
        for nxt in (curr * 2, curr * 10 + 1) :
            # 목표값에 도달했다면 바로 반환
            if nxt == e :
                return cnt + 1
            
            # 범위를 벗어나거나 이미 방문했다면 스킵
            if nxt > e or nxt in v :
                continue

            v.add(nxt)
            q.append((nxt, cnt + 1))

    return -1   # 목표값에 도달할 수 없는 경우

A, B = map(int, input().split())
print(bfs(A, B))