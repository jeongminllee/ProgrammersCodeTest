from collections import deque

def bfs(si, sj) :
    q = deque()
    q.append((si, sj, 0, 0))   # si, sj, cnt
    check = [[[0] * (1 << 6) for _ in range(M)] for _ in range(N)]
    check[si][sj][0] = 1

    while q :
        ci, cj, cnt, key = q.popleft()
        if arr[ci][cj] == '1' :
            return cnt

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M :
                if not check[ni][nj][key] :
                    if arr[ni][nj] == '1' or arr[ni][nj] == '.' :
                        check[ni][nj][key] = True
                        q.append((ni, nj, cnt + 1, key))
                    elif arr[ni][nj] in keys :
                        tmp_key = key|(1 << (ord(arr[ni][nj]) - ord('a')))
                        check[ni][nj][tmp_key] = 1
                        q.append((ni, nj, cnt + 1, tmp_key))
                    elif arr[ni][nj] in doors :
                        if key & (1 << (ord(arr[ni][nj]) - ord('A'))) :
                            check[ni][nj][key] = True
                            q.append((ni, nj, cnt + 1, key))
    return -1

N, M = map(int, input().split())    # 세로, 가로
arr = [list(input()) for _ in range(N)]

keys = set(['a', 'b', 'c', 'd', 'e', 'f'])
doors = set(['A', 'B', 'C', 'D', 'E', 'F'])

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == '0' :
            si, sj = i, j
            arr[i][j] = '.'

res = bfs(si, sj)
print(res)