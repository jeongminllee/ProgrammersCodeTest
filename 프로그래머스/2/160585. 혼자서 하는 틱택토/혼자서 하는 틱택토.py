def check(board, t) :
    win_conditions = []
    # 가로 승리 조건
    for i in range(3) :
        win_conditions.append([(i, j) for j in range(3)])
    # 세로 승리 조건
    for j in range(3) :
        win_conditions.append([(i, j) for i in range(3)])
    # 대각 승리 조건
    win_conditions.append([(i,i) for i in range(3)])
    win_conditions.append([(i,2-i) for i in range(3)])
    
    # 
    for condition in win_conditions :
        if all(board[x][y] == t for x, y in condition) :
            return True
    return False


def solution(board):
    # 문자열 배열 => 리스트
    board = [list(row) for row in board]
    ocnt = sum(row.count("O") for row in board)
    xcnt = sum(row.count("X") for row in board)
    
    # "O" "X" 개수 확인
    if not (ocnt == xcnt or ocnt == xcnt + 1) :
        return 0
    
    owin = check(board, "O")
    xwin = check(board, "X")
    
    # 승리 조건 확인
    if owin and xwin :  # 동시 승리 불가능
        return 0
    if owin and ocnt != xcnt + 1:  # O가 이겼을 떄
        return 0
    if xwin and ocnt != xcnt :  # X가 이겼을때
        return 0
    
    return 1