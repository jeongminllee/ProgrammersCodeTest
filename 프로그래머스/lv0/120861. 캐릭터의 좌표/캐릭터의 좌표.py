def solution(keyinput, board):
    answer = [0, 0]
    for key in keyinput :
        if key == 'left' :
            answer[0] = answer[0] - 1
            if abs(answer[0]) > abs(board[0] // 2) :
                answer[0] = - (board[0] // 2)
        elif key == 'right' :
            answer[0] = answer[0] + 1
            if abs(answer[0]) > abs(board[0] // 2) :
                answer[0] = board[0] // 2
        elif key == 'up' :
            answer[1] = answer[1] + 1
            if abs(answer[1]) > abs(board[1] // 2) :
                answer[1] = board[1] // 2
        else :
            answer[1] = answer[1] - 1
            if abs(answer[1]) > abs(board[1] // 2) :
                answer[1] = - (board[1] // 2)

    return answer