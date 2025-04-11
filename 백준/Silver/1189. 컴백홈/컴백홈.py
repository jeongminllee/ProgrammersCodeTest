def sol_1189() :
    R, C, K = map(int, input().split())
    maps = [list(input()) for _ in range(R)]

    target = (0, C - 1)

    visited = [[0] * K for _ in range(R)]

    res = 0

    def dfs(si, sj, cnt) :
        nonlocal res

        if (si, sj) == target and cnt == K :
            res += 1

        else :
            visited[si][sj] = 1

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
                ni, nj = si + di, sj + dj
                if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0 and maps[ni][nj] == '.' :
                    visited[ni][nj] = 1
                    dfs(ni, nj, cnt + 1)
                    visited[ni][nj] = 0
    dfs(R-1, 0, 1)
    print(res)

sol_1189()