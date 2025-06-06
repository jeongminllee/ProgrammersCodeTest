max_num = 0
chart = (0, 0)
board = []
for i in range(9) :
    board.append(list(map(int, input().split())))

for i in range(9) :
    for j in range(9) :
        if max_num < board[i][j] :
            max_num = board[i][j]
            chart = (i, j)

print(max_num)
print(chart[0] + 1, chart[1] + 1)