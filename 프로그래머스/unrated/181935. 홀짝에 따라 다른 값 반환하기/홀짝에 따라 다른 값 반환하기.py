def solution(n):
    answer = 0
    if n % 2 == 0:
        for m in range(1, n + 1):
            if m % 2 == 0:
                answer += (m ** 2)
    
    elif n % 2 != 0:
        for m in range(1, n + 1):
            if m % 2 != 0:
                answer += m
            
    return answer