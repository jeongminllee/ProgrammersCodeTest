def solution(x1, x2, x3, x4):
    answer = True
    a = x1 + x2
    b = x3 + x4
    answer = a + b
    if x1 == True or x2 == True :
        a = True
    else :
        a = False
    if x3 == True or x4 == True :
        b = True
    else :
        b = False
        
    if a == True and b == True :
        answer = True
    else :
        answer = False
    return answer