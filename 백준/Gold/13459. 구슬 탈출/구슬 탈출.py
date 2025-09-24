di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def move(i, j, dr) :
    back = -1
    for cnt in range(1, 10):    # 최대로 뻗어가서 벽 만날때 까지 진행
        ni, nj = i + di[dr] * cnt, j + dj[dr] * cnt
        if arr[ni][nj] == '#' : # 벽
            return cnt + back
        elif arr[ni][nj] == 'O' : # 아웃
            return cnt
        # 다른 공을 지나간 경우 벽을 만났다면 한 칸 뒤로
        if arr[ni][nj] == 'B' or arr[ni][nj] == 'R' :
            back -= 1

# DFS
def dfs(n, ri, rj, bi, bj) :
    global res
    if (n, ri, rj, bi, bj) in v_set :   # 이미 방문했음
        return
    v_set.add((n, ri, rj, bi, bj))      # 방문 처리

    if n > 10 : # 종료 조건
        return

    for dr in range(4) :            # 4방향 구슬들 이동
        # [1] 각 공의 이동거리 계산
        r_cnt = move(ri, rj, dr)
        b_cnt = move(bi, bj, dr)

        if r_cnt == 0 and b_cnt == 0 :  # 이 방향으로는 탐색 필요 없음
            continue

        # [2] 각 공의 이동 반영
        nri, nrj = ri + di[dr] * r_cnt, rj + dj[dr] * r_cnt # 이동 반영
        nbi, nbj = bi + di[dr] * b_cnt, bj + dj[dr] * b_cnt

        # [3] 이동한 위치가 홀인 경우 처리
        if arr[nbi][nbj] == 'O' :   # 파란색 공이 홀인 => 실패
            continue
        elif arr[nri][nrj] == 'O' : # 빨간색 공만 홀인 => 성공
            res = min(res, n)
            return

        # [4] 둘 다 홀이 아닌 경우 (next 좌표 기준으로 다음 시도)
        # 현재 위치를 빈칸, 이동할 위치에 "R", "B" 구슬 표시
        arr[ri][rj], arr[bi][bj] = ".", "."
        arr[nri][nrj], arr[nbi][nbj] = "R", "B"
        dfs(n+1, nri, nrj, nbi, nbj)
        arr[nri][nrj], arr[nbi][nbj] = ".", "."
        arr[ri][rj], arr[bi][bj] = "R", "B"

###### 입력
N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 'R' :
            ri, rj = i, j
        if arr[i][j] == 'B' :
            bi, bj = i, j

v_set = set()
res = 11
dfs(1, ri, rj, bi, bj)

if res == 11 :
    print(0)
else :
    print(1)