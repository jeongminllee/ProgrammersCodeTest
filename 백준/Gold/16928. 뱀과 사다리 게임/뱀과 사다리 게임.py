from collections import deque

def bfs(arr) :
    # BFS 시작 설정
    q = deque()
    q.append((1, 0))     # 현재 위치, 주사위 굴린 횟수
    visited = [0] * 101
    visited[1] = 1

    # BFS 실행
    while q :
        pos, cnt = q.popleft()
        if pos == 100 :
            return cnt  # 100번째 칸에 도착하면 주사위 굴린 횟수 반환
        for i in range(1, 7) :  # 주사위 1 ~ 6
            n_pos = pos + i
            if n_pos <= 100 and visited[n_pos] == 0 :
                visited[n_pos] = 1
                if arr[n_pos] != 0 :    # 사다리나 뱀이 있는 경우
                    n_pos = arr[n_pos]
                q.append((n_pos, cnt + 1))
    return -1

# 정답 처리
N, M = map(int, input().split())
arr = [0] * 101     # 게임판 초기화 (0은 뱀이나 사다리가 없는 칸을 의미

for _ in range(N + M):
    x, y = map(int, input().split())
    arr[x] = y      # 사다리 또는 뱀 정보 저장

print(bfs(arr))