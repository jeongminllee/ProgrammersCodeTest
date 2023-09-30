def solution(n):
    if n == 1 :
        return [[1]]
    
    answer = [[0 for j in range(n)] for i in range(n)]
    
    x = 0
    y = 0
    di = 'r'
    
    for i in range(n * n) :
        answer[x][y] = i + 1
        if di == 'r' :
            y += 1
            if y == n - 1 or answer[x][y + 1] != 0 :
                di = 'd'
        elif di == 'd' : 
            x += 1
            if x == n - 1 or answer[x + 1][y] != 0 :
                di = 'l'
        elif di == 'l' :
            y -= 1
            if y == 0 or answer[x][y - 1] != 0 :
                di = 'u'
        elif di == 'u' :
            x -= 1
            if x == n - 1 or answer[x - 1][y] != 0 :
                di = 'r'
            
    return answer