from collections import deque

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def bfs(si, sj, ei, ej) :
    INF = 10**9
    # dist[dir][i][j] : (i, j)에 dir 방향으로 들어왔을 때 필요한 최소 거울 수
    dist = [[[INF] * N for _ in range(N)] for _ in range(4)]
    q = deque()

    # 시작 칸에서 4방향 모두 비용 0으로 시작
    for d in range(4) :
        dist[d][si][sj] = 0
        q.append((si, sj, d))

    while q:
        ci, cj, dr = q.popleft()

        # 직진(0비용) : 현재 방향으로만 한 칸 전진
        ni, nj = ci + di[dr], cj + dj[dr]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '*' :
            # 0비용 갱신 -> appendleft
            if dist[dr][ni][nj] > dist[dr][ci][cj] :
                dist[dr][ni][nj] = dist[dr][ci][cj]
                q.appendleft((ni, nj, dr))

            # 거울 설치 간으 칸이면 1비용으로 직각 전환
            if arr[ni][nj] == '!' :
                # dr가 짝수면 홀수, 홀수면 짝수로 수직
                turn_dirs = (1, 3) if dr % 2 == 0 else (0, 2)
                for nd in turn_dirs :
                    if dist[nd][ni][nj] > dist[dr][ci][cj] + 1 :
                        dist[nd][ni][nj] = dist[dr][ci][cj] + 1
                        q.append((ni, nj, nd))

    res = min(dist[d][ei][ej] for d in range(4))
    return res
    
N = int(input())
arr = [list(input().strip()) for _ in range(N)]

# "#" : 문이 설치된 곳, 항상 2개
# "." : 아무 것도 없는 곳으로 빛이 통과함
# "!" : 거울 설치할 수 있는 위치
# "*" : 빛이 통과할 수 없는 벽

# 거울을 설치하면 무조건 직각으로 꺾여야함. 
# 그 방향이 2개로 나누어짐.
doors = []
# 문 좌표 넣기
for i in range(N) :
    for j in range(N) :
        if arr[i][j] == '#' :     # 문 좌표 
            doors.append((i, j))
            
(si, sj), (ei, ej) = doors    # 문은 2개 확정이기 때문에
print(bfs(si, sj, ei, ej))