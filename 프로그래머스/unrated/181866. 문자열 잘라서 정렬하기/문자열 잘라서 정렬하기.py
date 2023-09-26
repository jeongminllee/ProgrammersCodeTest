def solution(myString):
    answer = []
    for x in myString.split('x') :
        if x != '' :
            answer.append(x)
    return sorted(answer)


def solution(myString) :
    return sorted(' '.join(myString.split('x')).split())