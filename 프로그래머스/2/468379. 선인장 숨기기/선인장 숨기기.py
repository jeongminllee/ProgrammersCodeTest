"""
arr: m*n
arr_sun: h*w
drops: index = 각 위치별 비 내리는 순서

"""
from collections import deque

INF = 1<<32
def solution(m, n, h, w, drops):
    drops = [[-1, -1]] + drops
    
    arr = [[INF] * n for _ in range(m)]
    
    for idx, (i, j) in enumerate(drops[1:], 1) :
        arr[i][j] = idx
        
    answer = 0
            
    total_min = []
    
    col_min = []
    # 1. width 계산
    width = n - w + 1
    
    row_min = [[0] * width for _ in range(m)]
    
    for r in range(m) :
        q = deque()
        
        for c in range(n) :
            
            # window 밖 인덱스 제거
            while q and q[0] <= c-w :
                q.popleft()
                
            # 현재 값보다 크거나 같은 값 제거
            while q and arr[r][q[-1]] >= arr[r][c] :
                q.pop()
                
            q.append(c)
            
            if c >= w - 1 :
                left = c - w + 1
                row_min[r][left] = arr[r][q[0]]
                
    # 2. 세로 계산
    best = -1
    best_r = best_c = 0
    
    for c in range(width) :
        q = deque()
        
        for r in range(m) :
            
            # window 밖 인덱스 제거
            while q and q[0] <= r - h :
                q.popleft()
                
            # 현재 값보다 크거나 같은 값 제거
            while q and row_min[q[-1]][c] >= row_min[r][c] :
                q.pop()
                
            q.append(r)
            
            if r >= h - 1:
                top = r - h + 1
                
                score = row_min[q[0]][c]
                
                if score > best :
                    best = score
                    best_r = top
                    best_c = c
                    
                elif score == best :
                    if top < best_r :
                        best_r = top
                        best_c = c
                    elif top == best_r and c < best_c :
                        best_c = c
                        
    return [best_r, best_c]