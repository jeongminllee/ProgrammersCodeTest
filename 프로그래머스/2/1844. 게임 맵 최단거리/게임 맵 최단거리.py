from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]    
                
def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque()
    v = [[0] * m for _ in range(n)]
    
    q.append((0, 0))
    v[0][0] = 1
    
    while q :
        ci, cj = q.popleft()
        if (ci, cj) == (n-1, m-1) :
            return v[ci][cj]
        
        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and v[ni][nj] == 0 :
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
                
    return -1
    
    