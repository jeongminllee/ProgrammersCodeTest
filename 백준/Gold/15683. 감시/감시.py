dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]  # 남, 동, 북, 서

def OOB(a, b) : # Out of Bounds 변수
    return a < 0 or a >= n or b < 0 or b >= m

def upd(x, y, dir) :
    dir %= 4
    while True :
        x += dx[dir]
        y += dy[dir]
        if OOB(x, y) or board2[x][y] == 6 :
            return  # 범위를 벗어났거나 벽을 만나면 함수를 탈출
        if board2[x][y] != 0 :
            continue    # 해당 칸이 빈칸이 아닐경우(=cctv가 있을 경우) 넘어감
        board2[x][y] = 7    # 빈칸을 7로 덮음

def main() :
    global n, m, board1, board2, cctv
    n, m = map(int, input().split())
    mn = 0  # 사각 지대의 최소 크기 (=답)
    board1 = [list(map(int, input().split())) for _ in range(n)]    # 최초에 입력받은 board를 저장할 변수
    board2 = [[0] * m for _ in range(n)]                            # 사각지대의 개수를 세기 위해 사용할 변수
    cctv = []                                                       # cctv의 좌표를 저장할 변수

    for i in range(n) :
        for j in range(m) :
            if 0 < board1[i][j] < 6 :
                cctv.append((i, j))
            if board1[i][j] == 0 :
                mn += 1


    for tmp in range(4 ** len(cctv)) :  # 4의 cctv 개수 제곱만큼 반복
        for i in range(n) :
            for j in range(m) :
                board2[i][j] = board1[i][j] # deepcopy

        brute = tmp
        for i, (x, y) in enumerate(cctv) :
            dir = brute % 4
            brute //= 4
            if board1[x][y] == 1 :
                upd(x, y, dir)
            elif board1[x][y] == 2 :
                upd(x, y, dir)
                upd(x, y, dir+2)
            elif board1[x][y] == 3:
                upd(x, y, dir)
                upd(x, y, dir + 1)
            elif board1[x][y] == 4 :
                upd(x, y, dir)
                upd(x, y, dir+1)
                upd(x, y, dir+2)
            else :  # board1[x][y] == 5 :
                upd(x, y, dir)
                upd(x, y, dir + 1)
                upd(x, y, dir + 2)
                upd(x, y, dir+3)


        val = sum(row.count(0) for row in board2)
        mn = min(mn, val)

    print(mn)

if __name__ == "__main__" :
    main()