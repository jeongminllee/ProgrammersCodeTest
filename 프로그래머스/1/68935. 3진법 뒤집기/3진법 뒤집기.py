def solution(n):
    answer = 0
    rev_num = []
    
    while n > 0 :
        rev_num.append(n % 3)
        n //= 3
        
    for i in range(len(rev_num)) :
        answer += 3 ** (len(rev_num) - i - 1) * rev_num[i]
        
    return answer