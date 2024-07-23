import sys
input = sys.stdin.readline

def dfs(i, j) :
    # 도착 지점에 도달하면 1을 리턴(이건 OK)
    if (i, j) == (N-1, M-1) :
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴(이건 무슨 말이지? 분기점 잡는건가)
    if v[i][j] != -1 :
        return v[i][j]

    cnt = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] < arr[i][j] :
            cnt += dfs(ni, nj)

    v[i][j] = cnt
    return v[i][j]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[-1] * M for _ in range(N)]
print(dfs(0, 0))