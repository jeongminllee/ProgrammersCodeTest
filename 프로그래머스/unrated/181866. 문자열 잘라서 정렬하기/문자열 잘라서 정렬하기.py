def solution(myString):
    answer = []
    for x in myString.split('x') :
        if x != '' :
            answer.append(x)
    return sorted(answer)