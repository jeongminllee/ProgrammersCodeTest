from collections import deque

def bfs(s) :
    v = [[0] * n for _ in range(n)]
    q = deque()
    q.append(s)
    v[s[0]][s[1]] = 1
    distance = 0
    fish = []
    while q:
        for _ in range(len(q)) :
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0 :
                    if arr[nx][ny] <= shark_size or arr[nx][ny] == 0 :
                        q.append((nx, ny))
                        v[nx][ny] = 1
                        if 0 < arr[nx][ny] < shark_size :
                            fish.append((nx, ny))
        distance += 1
        if fish :
            fish.sort()
            return fish[0], distance
    return None, None

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 9 :
            shark_pos = (i, j)
            arr[i][j] = 0

shark_size = 2
cnt = 0
time = 0

while 1 :
    fish_pos, distance = bfs(shark_pos)
    if fish_pos is None :
        break

    arr[fish_pos[0]][fish_pos[1]] = 0
    cnt += 1
    time += distance
    shark_pos = fish_pos
    if cnt == shark_size :
        shark_size += 1
        cnt = 0

print(time)