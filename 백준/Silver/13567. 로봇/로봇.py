# 0, 1 => 왼쪽으로 90, 오른쪽으로 90 =>
# 처음엔 [i+1][j]
# => 0 [i][j+1] => [i-1][j] => [i][j-1]
# => 1 [i][j-1] => [i-1][j] => [i][j+1]
# di, dj = (1, 0), (0, 1), (-1, 0), (0, -1)
# 0이면 -> 순으로, 1이면 <- 순으로...

M, n = map(int, input().split())
arr = [[0] * (M + 1) for _ in range(M + 1)]

dir = 0
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
pos = [0, 0]
flag = True

for i in range(n) :
    mode, num = input().split()

    if mode == "MOVE" :
        pos[0] += di[dir] * int(num)
        pos[1] += dj[dir] * int(num)

    else :
        if num == '0' :
            dir = (dir + 1) % 4
        else :
            dir = (dir - 1) % 4

    if not (0 <= pos[0] < M and 0 <= pos[1] < M) :
        flag = False
        break

if flag == False :
    print(-1)
else :
    print(' '.join(map(str, pos)))