def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1) :   # idx 추출
        # idx에서 len p 까지만 추출
        if int(t[i:i + len(p)]) <= int(p) : 
            answer += 1
    return answer