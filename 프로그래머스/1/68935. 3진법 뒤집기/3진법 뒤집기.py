# n % 3 으로 3진법을 표현함. 
# str 으로 받은 다음 reverse 로 하고 3 ** (저거)를 하면 되지 않을까?
def solution(n):
    answer = 0
    rev_num = []
    
    while n > 0 :
        rev_num.append(n % 3)
        n //= 3
        
    for i in range(len(rev_num)) :
        answer += 3 ** (len(rev_num) - i - 1) * rev_num[i]
        
    return answer