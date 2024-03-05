from collections import deque

def bfs() :
    # q 생성, v[] 생성
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]

    # q에 초기 데이터(들) 삽입, 안 익은 토마토 카운트
    cnt = 0    # 안 익은 토마토
    for h in range(H) :    # 전체 순회
        for i in range(N) :
            for j in range(M) :
                if arr[h][i][j] == 1 :
                    q.append((h, i, j))    # 초기 데이터 삽입
                    v[h][i][j] = 1

                elif arr[h][i][j] == 0 :    # 안 익은 토마토
                    cnt += 1

    while q :
        ch, ci, cj = q.popleft()

        # 6방향, 범위 내, 미방문, arr[] == 0 
        for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)) :
            nh, ni, nj = ch + dh, ci + di, cj + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and v[nh][ni][nj] == 0 and arr[nh][ni][nj] == 0 :
                q.append((nh, ni, nj))
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                cnt -= 1

    if cnt == 0 :    # 토마토가 모두 익었다면
        return v[ch][ci][cj] - 1

    else :
        return -1

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
print(bfs())