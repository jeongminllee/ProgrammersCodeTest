def get_max_tetromino_sum(N, M, board):
    # 모든 테트로미노 모양 정의
    tetrominos = [
        # ㅡ 모양
        [(0,0), (0,1), (0,2), (0,3)],
        [(0,0), (1,0), (2,0), (3,0)],
        
        # ㅁ 모양
        [(0,0), (0,1), (1,0), (1,1)],
        
        # L 모양
        [(0,0), (1,0), (2,0), (2,1)],
        [(0,0), (0,1), (0,2), (1,0)],
        [(0,0), (0,1), (1,1), (2,1)],
        [(0,2), (1,0), (1,1), (1,2)],
        [(0,1), (1,1), (2,0), (2,1)],
        [(0,0), (1,0), (1,1), (1,2)],
        [(0,0), (0,1), (1,0), (2,0)],
        [(0,0), (0,1), (0,2), (1,2)],
        
        # ㄹ 모양
        [(0,0), (1,0), (1,1), (2,1)],
        [(0,1), (0,2), (1,0), (1,1)],
        [(0,1), (1,0), (1,1), (2,0)],
        [(0,0), (0,1), (1,1), (1,2)],
        
        # ㅜ 모양
        [(0,0), (0,1), (0,2), (1,1)],
        [(0,1), (1,0), (1,1), (2,1)],
        [(0,1), (1,0), (1,1), (1,2)],
        [(0,0), (1,0), (1,1), (2,0)]
    ]
    
    def is_valid(x, y, tetromino):
        for dx, dy in tetromino:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                return False
        return True
    
    def get_sum(x, y, tetromino):
        total = 0
        for dx, dy in tetromino:
            total += board[x + dx][y + dy]
        return total
    
    max_sum = 0
    # 모든 위치에서 모든 테트로미노 모양을 시도
    for i in range(N):
        for j in range(M):
            for tetromino in tetrominos:
                if is_valid(i, j, tetromino):
                    current_sum = get_sum(i, j, tetromino)
                    max_sum = max(max_sum, current_sum)
    
    return max_sum

# 입력 처리
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = get_max_tetromino_sum(N, M, board)
print(result)