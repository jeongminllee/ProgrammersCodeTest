from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def in_range(i, j, N) :
    return 0<=i<N and 0<=j<N

def go_dest(i, j, N, board, passengers) :
    dest_i, dest_j = passengers[(i, j)]
    del passengers[(i, j)]
    q = deque()
    q.append((i, j, 0))
    visited = set()
    visited.add((i, j))

    while q :
        ci, cj, cnt = q.popleft()
        if (ci, cj) == (dest_i, dest_j) :
            return ci, cj, cnt
        for d in range(4) :
            ni, nj, nxt = ci + di[d], cj + dj[d], cnt + 1
            if (ni, nj) in visited :
                continue
            if in_range(ni, nj, N) and board[ni][nj] != 1 :
                q.append((ni, nj, nxt))
                visited.add((ni, nj))

    return dest_i, dest_j, 10 ** 8


def bfs(N, M, fuels, board, si, sj, passengers) :
    q = deque()
    q.append((si, sj, 0))
    visited = set()
    visited.add((si, sj))
    candidate = []
    min_distance = 10 ** 8

    while q :
        ci, cj, cnt = q.popleft()
        if cnt > min_distance :
            break

        if (ci, cj) in passengers :
            candidate.append((ci, cj))
            min_distance = cnt

        for d in range(4) :
            ni, nj, nxt = ci + di[d], cj + dj[d], cnt + 1
            if (ni, nj) in visited :
                continue

            if in_range(ni, nj, N) and board[ni][nj] != 1 :
                q.append((ni, nj, nxt))
                visited.add((ni, nj))

    return candidate, min_distance

def main() :
    N, M, fuels = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    si, sj = map(int, input().split())
    si, sj = si-1, sj-1
    passengers = {}

    for _ in range(M) :
        p1, p2, p3, p4 = map(int, input().split())
        passengers[(p1-1, p2-1)] = (p3-1, p4-1)

    answer = 0

    while fuels > 0 and len(passengers) != 0 :
        cand, used_feul = bfs(N, M, fuels, board, si, sj, passengers)
        if used_feul > fuels or len(cand) == 0 :
            answer = -1
            break

        si, sj = sorted(cand)[0]

        fuels -= used_feul
        dest_i, dest_j, used_feul = go_dest(si, sj, N, board, passengers)
        if used_feul > fuels :
            answer -= 1
            break
        fuels += used_feul
        si, sj = dest_i, dest_j

    if answer == -1 :
        return -1
    else :
        return fuels

if __name__ == "__main__" :
    print(main())