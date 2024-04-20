from math import floor, ceil, sqrt
def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1) :
        if i < r1 :
            answer += floor(sqrt(r2**2 - i**2)) - ceil(sqrt(r1**2 - i**2))+1
        else :
            answer += floor(sqrt(r2**2 - i**2)) + 1

    answer *= 4
    return answer