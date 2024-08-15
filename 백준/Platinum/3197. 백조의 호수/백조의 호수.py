from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

in_range = lambda y, x : 0 <= y < R and 0 <= x < C
def find(v) :
    if v == edges[v[0]][v[1]] :
        return v

    edges[v[0]][v[1]] = find(edges[v[0]][v[1]])
    return edges[v[0]][v[1]]

def union(v1, v2) :
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1[0]][r1[1]] > rank[r2[0]][r2[1]] :
        edges[r2[0]][r2[1]] = r1

    elif rank[r1[0]][r1[1]] < rank[r2[0]][r2[1]] :
        edges[r1[0]][r1[1]] = r2

    else :
        edges[r2[0]][r2[1]] = r1
        rank[r1[0]][r1[1]] += 1

R, C = map(int, input().split())

maps = [list(input()) for _ in range(R)]
edges = [[(i, j) for j in range(C)] for i in range(R)]
rank = [[0] * C for _ in range(R)]
visit = [[0] * C for _ in range(R)]
swan = []

for i in range(R) :
    for j in range(C) :
        if maps[i][j] == "L" :
            swan.append((i, j))
            maps[i][j] = '.'
            if len(swan) == 2 :
                break

melt = deque()
for i in range(R) :
    for j in range(C) :
        if not visit[i][j] and maps[i][j] == '.' :
            q = deque()
            q.append((i, j))
            visit[i][j] = 1

            while q :
                ci, cj = q.popleft()
                edges[ci][cj] = (i, j)

                for d in range(4) :
                    ni, nj = ci + di[d], cj + dj[d]

                    if in_range(ni, nj) and not visit[ni][nj] :
                        if maps[ni][nj] == '.' :
                            visit[ni][nj] = 1
                            q.append((ni,nj))

                        elif maps[ni][nj] == 'X' :
                            visit[ni][nj] = 1
                            melt.append((ni, nj))

day = 0
while find(swan[0]) != find(swan[1]) :
    tmp = deque()
    while melt :
        ci, cj = melt.popleft()
        maps[ci][cj] = '.'
        merge_point = []

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if in_range(ni, nj) :
                if not visit[ni][nj] and maps[ni][nj] == 'X':
                    visit[ni][nj] = 1
                    tmp.append((ni, nj))

                elif maps[ni][nj] == '.':
                    merge_point.append((ni, nj))

        for p in merge_point :
            if find(p) != find((ci, cj)) :
                union(p, (ci, cj))

    melt = tmp
    day += 1

print(day)