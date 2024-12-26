from collections import deque

def bfs(si, sj, graph):
    """
    너비 우선 탐색(BFS)을 사용하여 시작점(0,0)에서 목표 지점까지의 최단 거리를 찾는 함수
    si, sj: 시작점의 좌표
    graph: 이동 가능한 좌표들의 집합
    반환값: 목표 지점까지의 최단 이동 횟수 또는 도달 불가능할 경우 -1
    """
    # 큐 초기화 및 시작점 추가
    # (i좌표, j좌표, 이동 횟수)를 튜플로 저장
    q = deque()
    q.append((si, sj, 0))

    while q:
        # 현재 위치와 여기까지 오는데 걸린 이동 횟수를 가져옴
        ci, cj, cnt = q.popleft()

        # 현재 j좌표가 목표 지점(T)에 도달했다면 이동 횟수 반환
        if cj == T:
            return cnt

        # 상하좌우 및 대각선을 포함한 주변 25개 칸을 탐색 (-2 ~ +2 범위)
        for di in range(-2, 3):
            for dj in range(-2, 3):
                # 다음 이동할 좌표 계산
                ni, nj = ci + di, cj + dj
                
                # 다음 좌표가 이동 가능한 좌표 집합에 있는 경우
                if (ni, nj) in graph:
                    # 해당 좌표를 큐에 추가하고 방문 처리
                    q.append((ni, nj, cnt + 1))
                    # 방문한 좌표는 graph에서 제거하여 중복 방문 방지
                    graph.remove((ni, nj))
    
    # 목표 지점에 도달할 수 없는 경우 -1 반환
    return -1

# 입력 받기
# n: 이동 가능한 좌표의 개수
# T: 목표 지점의 j좌표 (x축 값)
n, T = map(int, input().split())

# 이동 가능한 좌표들을 집합으로 저장
# 집합을 사용하여 좌표 존재 여부를 O(1) 시간에 확인 가능
graph = set()
for _ in range(n):
    graph.add(tuple(map(int, input().split())))

# BFS 실행 및 결과 출력
res = bfs(0, 0, graph)
print(res)