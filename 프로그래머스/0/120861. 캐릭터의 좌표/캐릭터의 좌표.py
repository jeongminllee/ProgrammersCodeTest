dr = {
    'left' : [-1, 0],
    'right' : [1, 0],
    'up' : [0, 1],
    'down' : [0, -1]
}

def solution(keyinput, board):
    limit_x = board[0] // 2
    limit_y = board[1] // 2

    x, y = 0, 0
    for key in keyinput :
        nx, ny = x + dr[key][0], y + dr[key][1]

        if -limit_x <= nx <= limit_x and -limit_y <= ny <= limit_y :
            x = nx
            y = ny

    answer = [x, y]
    return answer