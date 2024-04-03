from collections import deque
def bfs(si, sj, v, maps, n, m) :
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1
    cnt = int(maps[si][sj])
    
    while q:
        ci, cj = q.popleft()
        
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and maps[ni][nj] != "X" :
                v[ni][nj] = 1
                cnt += int(maps[ni][nj])
                q.append((ni, nj))
    return cnt
    

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    v = [[0] * m for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            if v[i][j] == 0 and maps[i][j] != "X" :
                answer.append(bfs(i, j, v, maps, n, m))
    return sorted(answer) if answer else [-1]