def solution(balls, share):
    answer = 0
    n = 1
    m = 1
    o = 0
    
    for ball in range(balls, 0, -1) :
        n *= ball
        o += 1
        if o == share :
            break
    for sha in range(share, 0, -1) :
        m *= sha
        
        print(n)
        print(m)
        print(o)
        answer = n // m
        print(answer)
    return answer