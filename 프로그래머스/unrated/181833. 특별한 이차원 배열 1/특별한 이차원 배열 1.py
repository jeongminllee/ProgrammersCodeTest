# def solution(n):
#     return [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    
def solution(n) :
    answer = [[0] * n for _ in range(n)]
    
    for i in range(n) : 
        answer[i][i] = 1
        
    return answer