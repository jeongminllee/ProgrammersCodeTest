def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for a_or_h, r1, c1, r2, c2, degree in skill :
        if a_or_h == 1 :
            degree = -degree
        
        prefix_sum[r1][c1] += degree
        prefix_sum[r2+1][c2+1] += degree
        prefix_sum[r2+1][c1] -= degree
        prefix_sum[r1][c2+1] -= degree
        
    # print(*prefix_sum, sep='\n')
    # print('=' * 10)
    for i in range(n+1) :
        for j in range(m) :
            prefix_sum[i][j+1] += prefix_sum[i][j]
    
    for j in range(m+1) :
        for i in range(n) :
            prefix_sum[i+1][j] += prefix_sum[i][j]
            
    # print(*prefix_sum, sep='\n')
    
    for i in range(n) :
        for j in range(m) :
            board[i][j] += prefix_sum[i][j]
            if board[i][j] > 0 :
                answer += 1
                
    return answer