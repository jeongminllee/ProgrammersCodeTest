def solution(dots):
    answer = 0
    b1 = 0
    b2 = 0
    for i, d in enumerate(dots) :
        a1 = dots[0]
        a2 = dots[1]
        a3 = dots[2]
        a4 = dots[3]
        if a1[0] == a2[0] :
            b1 = abs(a1[1] - a2[1])
            b2 = abs(a2[0] - a3[0])
        else :
            b1 = abs(a1[0] - a2[0])
            b2 = abs(a2[1] - a3[1])
    answer = b1 * b2
    return answer

# def solution(dots):
#     return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])
