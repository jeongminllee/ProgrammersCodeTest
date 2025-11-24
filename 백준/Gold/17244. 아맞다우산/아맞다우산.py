from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, ei, ej, cnt) :
    q = deque()
    q.append((si, sj, 0))   # si, sj, 물건 갯수
    v[si][sj][0] = 0

    while q :
        ci, cj, bit = q.popleft()
        curr = v[ci][cj][bit]

        if (ci, cj) == (ei, ej) and bit == 2 ** cnt - 1:
            return curr

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < M and 0 <= nj < N and v[ni][nj][bit] == -1 :
                if arr[ni][nj] == "#" :
                    continue
                elif arr[ni][nj] == "X" :
                    nxt_bit = bit | (1<<tbl[(ni, nj)])
                    q.append((ni, nj, nxt_bit))
                    v[ni][nj][nxt_bit] = curr + 1
                else :
                    q.append((ni, nj, bit))
                    v[ni][nj][bit] = curr + 1

    return -1
\
def main() :
    global N, M, arr, v, tbl
    N, M = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(M)]
    cnt = 0
    si = sj = ei = ej = 0
    tbl = {}    # 중복 처리를 위해 물건 위치를 담자.
    for i in range(M) :
        for j in range(N) :
            if arr[i][j] == "S" :
                si, sj = i, j
                arr[si][sj] = "."
            elif arr[i][j] == "E" :
                ei, ej = i, j
            elif arr[i][j] == "X" :
                tbl[(i, j)] = cnt
                cnt += 1

    v = [[[-1 for _ in range(1<<cnt)] for _ in range(N)] for _ in range(M)]

    print(bfs(si, sj, ei, ej, cnt))

if __name__ == "__main__" :
    main()