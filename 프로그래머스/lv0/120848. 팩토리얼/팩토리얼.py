def solution(n):
    i = 0
    fac = 1
    while n >= fac :
        i += 1
        fac *= i
        
    return i - 1