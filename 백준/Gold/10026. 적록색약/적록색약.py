from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, arr, v) :
    N = len(arr)
    q = deque()
    q.append((si, sj))

    while q :
        ci, cj = q.popleft()

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == arr[ci][cj] and v[ni][nj] == 0 :
                q.append((ni, nj))
                v[ni][nj] = 1

def main() :
    """
    :return: [적록색약이 아닌 사람이 봤을 때의 구역의 개수, 적록색약인 사람이 봤을 때의 구역의 개수]
    """
    N = int(input())
    arr = [list(input().rstrip()) for _ in range(N)]
    normal = [[0 for _ in range(N)] for _ in range(N)]
    blind = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 'R' :
                normal[i][j] = 1
                blind[i][j] = 1
            elif arr[i][j] == 'G' :
                normal[i][j] = 2
                blind[i][j] = 1

    normal_v = [[0 for _ in range(N)] for _ in range(N)]
    blind_v = [[0 for _ in range(N)] for _ in range(N)]
    n_cnt = b_cnt = 0

    for i in range(N) :
        for j in range(N) :
            if normal_v[i][j] == 0 :
                bfs(i, j, normal, normal_v)
                n_cnt += 1

            if blind_v[i][j] == 0 :
                bfs(i, j, blind, blind_v)
                b_cnt += 1

    print(n_cnt, b_cnt)

if __name__ == "__main__" :
    main()