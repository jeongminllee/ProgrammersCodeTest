def solution(order):
    answer = 0
    for o in list(str(order)) :
        if o in '369' :
            answer += 1
    return answer