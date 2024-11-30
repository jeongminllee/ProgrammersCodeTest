# 0 : 빈칸
# 1 ~ 6 : 물고기의 크기
# 9 : 아기 상어의 위치
# 처음 아기 상어의 크기 2
# 상하좌우 인접한 한 칸씩 이동
# 아기 상어는 자기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지는 지나갈 수 있음.
# 자기보다 작은 물고기만 먹을 수 있음.
# => 크기가 같으면 먹을 순 없지만, 지나갈 순 있음.

# 먹을 수 있으면 그 물고기 먹으러 간다.
# 먹을 수 있는게 여러 마리면 그 중 가장 가까운 물고기를 먹으러 간다.
# 거리가 같으면, 가장 위에 있는 물고기, 가장 왼쪽의 물고기

# 이동은 1초가 걸리고 먹는데는 시간이 걸리지 않는다.

# 자신의 크기와 같은 수의 물고기를 먹으면 크기가 1 증가한다.

from collections import deque

def bfs(s, shark_size) :
    v = [[0] * n for _ in range(n)]
    q = deque()
    q.append(s)
    v[s[0]][s[1]] = 1
    distance = 0

    fish = []   # 먹을 수 있는 물고기 리스트

    while q :
        for _ in range(len(q)) :
            x, y = q.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0 :
                    if arr[nx][ny] <= shark_size or arr[nx][ny] == 0 :  # 상어가 이동할 수 있는 칸
                        q.append((nx, ny))
                        v[nx][ny] = 1
                        if 0 < arr[nx][ny] < shark_size :   # 먹을 수 있는 물고기
                            fish.append((nx, ny))

        distance += 1   # 이동
        # 가장 가까운 물고기 선택(거리, 위쪽, 왼쪽 순으로 정렬)
        if fish :
            fish.sort()
            return fish[0], distance    # x, y, distance

    return None, None

def simulation(arr) :
    # 아기 상어의 초기 위치 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                shark_pos = (i, j)
                arr[i][j] = 0   # 아기 상어 초기 위치를 빈칸으로 변경

    shark_size = 2  # 아기 상어의 초기 상태
    cnt = 0  # 아기 상어가 먹은 물고기 수.
    time = 0  # 이동 시간

    while True:
        fish_pos, distance = bfs(shark_pos, shark_size)
        if fish_pos is None:
            break   # 더 이상 먹을 물고기가 없음

        # 상어 이동 및 물고기 먹기
        arr[fish_pos[0]][fish_pos[1]] = 0
        cnt += 1
        time += distance
        shark_pos = fish_pos
        
        # 상어 크기 증가 조건
        if cnt == shark_size:
            shark_size += 1
            cnt = 0
    return time

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = simulation(arr)

print(res)