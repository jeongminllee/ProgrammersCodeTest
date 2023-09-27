def solution(hp):
    answer = 0
    n = 0
    m = 0
    o = 0
    while hp != 0 :
        if hp >= 5 :
            n += 1
            hp -= 5
        elif hp >= 3 :
            m += 1
            hp -= 3
        else : 
            o += 1
            hp -= 1
        answer = n + m + o
    return answer