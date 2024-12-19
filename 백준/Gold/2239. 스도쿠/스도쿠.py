def is_valid(num, row, col) :
    # 1. 현재 위치에 num이 들어갈 수 있는지 검사
    return not (in_row(num, row) or in_col(num, col) or in_box(num, row, col))

def in_row(num, row) :
    # 2. 해당 행에 num이 있는지 확인
    return num in board[row]

def in_col(num, col) :
    # 3. 해당 열에 num이 있는지 확인
    return num in (board[i][col] for i in range(9))

def in_box(num, row, col) :
    # 4. 현재 위치의 3x3 박스에 num이 있는지 확인
    box_row = (row//3) * 3
    box_col = (col//3) * 3

    for i in range(box_row, box_row + 3) :
        for j in range(box_col, box_col + 3) :
            if board[i][j] == num :
                return True

    return False

def find_empty_position() :
    # 5. 스도쿠 보드에 비어있는 위치 반환
    for i in range(9) :
        for j in range(9) :
            if board[i][j] == 0 :
                return i, j
    return None

def solve() :
    # 6. 비어 있는 위치에 가능한 숫자를 넣어가며 스도쿠 해결
    empty_pos = find_empty_position()
    # 7. 빈 칸이 없으면 스도쿠가 해결된 것으로 간주
    if not empty_pos :
        return True
    row, col = empty_pos
    for num in range(1, 10) :
        if is_valid(num, row, col) :
            board[row][col] = num
            if solve() :    # 8. 다음 빈 칸으로 재귀적으로 탐색
                return True
            board[row][col] = 0 # 9. 가능한 숫자가 없으면 원래의 0으로 되돌림
    return False

board = [list(map(int, input())) for _ in range(9)]
solve()
for i in board :
    print(*i, sep='')