def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m * t) :
        test += str(div(i, n))
        
    while len(answer) < t :
        answer += test[p-1]
        p += m
        
    return answer

def div(n, base) :
    digits = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0 :
        return digits[r]
    else :
        return div(q, base) + digits[r]