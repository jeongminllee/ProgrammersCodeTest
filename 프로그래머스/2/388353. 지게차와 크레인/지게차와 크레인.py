from collections import deque

def bfs(board, cmd, v) :
    q = deque()
    q.append((0, 0))  # i, j
    v[0][0] = 1
    
    while q :
        r, c = q.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and v[nr][nc] == 0 :
                v[nr][nc] = 1
                if board[nr][nc] == cmd :
                    pass
                elif board[nr][nc] == ' ' :
                    q.append((nr, nc))
    

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    answer = 0
    board = [[' ' for _ in range(m + 2)] for _ in range(n + 2)]
    
    for i in range(n) :
        for j in range(m) :
            board[i + 1][j + 1] = storage[i][j]
    
    for req in requests :
        cmd = req[0]
        crane = False
        if len(req) == 2 :
            for i in range(1, len(board) - 1) :
                for j in range(1, len(board[0]) - 1) :
                    if board[i][j] == cmd :
                        board[i][j] = ' '
        else :
            v = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
            bfs(board, cmd, v)
            for i in range(1, len(board) - 1) :
                for j in range(1, len(board[0]) - 1) :
                    if board[i][j] == cmd and v[i][j]:
                        board[i][j] = ' '
                    
    for i in range(1, len(board) - 1) :
        for j in range(1, len(board[0]) - 1) :
            if board[i][j] != ' ':
                answer += 1
    return answer