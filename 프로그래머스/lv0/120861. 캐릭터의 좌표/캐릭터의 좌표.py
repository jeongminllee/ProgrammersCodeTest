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



# def solution(keyinput, board):
#     x_lim,y_lim = board[0]//2,board[1]//2
#     move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
#     x,y = 0,0
#     for k in keyinput:
#         dx,dy = move[k]
#         if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
#             continue
#         else:
#             x,y = x+dx,y+dy

#     return [x,y]
