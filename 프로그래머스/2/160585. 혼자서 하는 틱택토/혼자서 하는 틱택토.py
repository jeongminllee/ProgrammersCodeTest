def check(board, t):
    win_conditions = []
    # 가로 승리 조건
    for i in range(3):
        win_conditions.append([(i, j) for j in range(3)])
    # 세로 승리 조건
    for j in range(3):
        win_conditions.append([(i, j) for i in range(3)])
    # 대각선 승리 조건
    win_conditions.append([(i, i) for i in range(3)])
    win_conditions.append([(i, 2 - i) for i in range(3)])

    # 승리 조건 충족 여부 확인
    for condition in win_conditions:
        if all(board[x][y] == t for x, y in condition):
            return True
    return False


def solution(board):
    board = [list(row) for row in board]  # 문자열 배열을 리스트로 변환
    ocnt = sum(row.count("O") for row in board)  # "O"의 개수
    xcnt = sum(row.count("X") for row in board)  # "X"의 개수

    # "O"와 "X"의 개수가 규칙에 부합하는지 확인
    if not (ocnt == xcnt or ocnt == xcnt + 1):
        return 0

    owin = check(board, "O")  # "O"의 승리 조건 충족 여부
    xwin = check(board, "X")  # "X"의 승리 조건 충족 여부

    # 승리 조건 검증
    if owin and xwin:  # 두 플레이어가 동시에 승리하는 것은 불가능
        return 0
    if owin and ocnt != xcnt + 1:  # "O"가 이겼다면, "O"의 개수는 "X"의 개수보다 하나 더 많아야 함
        return 0
    if xwin and ocnt != xcnt:  # "X"가 이겼다면, "O"와 "X"의 개수는 동일해야 함
        return 0

    return 1  # 위의 모든 조건을 만족하지 않으면 규칙에 부합하는 게임판 상태로 간주