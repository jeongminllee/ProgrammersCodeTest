def solution(board, skill):
    n, m, cnt = len(board), len(board[0]), 0
    ac_sum = [[0] * (m+1) for _ in range(n+1)]
    
    for at, r1, c1, r2, c2, degree in skill :
        val = 0
        if at == 1 :
            val = -degree
        else :
            val = degree
        
        ac_sum[r1][c1] += val
        ac_sum[r2+1][c2+1] += val
        ac_sum[r1][c2+1] -= val
        ac_sum[r2+1][c1] -= val
        
    for i in range(n+1) :
        for j in range(m) :
            ac_sum[i][j+1] += ac_sum[i][j]
    for j in range(m+1) :
        for i in range(n) :
            ac_sum[i+1][j] += ac_sum[i][j]
    
    for i in range(n) :
        for j in range(m) :
            board[i][j] += ac_sum[i][j]
            if board[i][j] > 0 :
                cnt += 1
                
    return cnt