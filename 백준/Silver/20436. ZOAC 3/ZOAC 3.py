sl, sr = input().split()
st = input()
board = [
    list(map(str, 'qwertyuiop')),
    list(map(str, 'asdfghjkl0')),
    list(map(str, 'zxcvbnm000'))
]
right = 'yuiophjklbnm'

xl, yl, xr, yr = 0, 0, 0, 0

for i in range(len(board)) :
    if sl in board[i] :
        xl = i
        yl = board[i].index(sl)

    if sr in board[i] :
        xr = i
        yr = board[i].index(sr)

cnt = 0
for s in st :
    cnt += 1
    if s in right :
        for i in range(len(board)) :
            if s in board[i] :
                nx = i
                ny = board[i].index(s)

                cnt += abs(nx - xr) + abs(ny - yr)
                xr = nx
                yr = ny
                break

    else :
        for i in range(len(board)) :
            if s in board[i] :
                nx = i
                ny = board[i].index(s)

                cnt += abs(nx - xl) + abs(ny - yl)
                xl = nx
                yl = ny
                break
print(cnt)