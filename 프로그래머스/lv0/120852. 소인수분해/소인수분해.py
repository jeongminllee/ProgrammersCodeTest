def solution(n):
    answer = []
    factor = []
    i = 2
    
    while i <= n :
        if n % i == 0 :
            factor.append(i)
            n = n // i 
        else :
            i += 1
            
    for i in factor :
        if i not in answer :
            answer.append(i)
            
    return answer