def solution(strArr):
    answer = []
    for i, arr in enumerate(strArr) :
        if i % 2 == 0 :
            answer.append(arr.lower())
        else :
            answer.append(arr.upper())
    return answer
