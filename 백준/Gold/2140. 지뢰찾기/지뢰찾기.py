# 상하좌우 및 대각선
dr = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

N = int(input())

arr = [list(input()) for _ in range(N)]

cnt = 0

def bomb(si, sj) :
    for d in range(8) :
        ni, nj = si + dr[d][0], sj + dr[d][1]
        if arr[ni][nj] != '#' and arr[ni][nj] != 'bomb' :
            arr[ni][nj] = str(int(arr[ni][nj]) - 1)

for i in range(N) :
    for j in range(N) :
        flag = 0
        if arr[i][j] == '#' :
            for d in range(8) :
                ni, nj = i + dr[d][0], j + dr[d][1]
                if arr[ni][nj] == '0' :
                    flag = 1
                    break
            if flag == 0 :
                bomb(i, j)
                arr[i][j] = 'bomb'
                cnt += 1

print(cnt)