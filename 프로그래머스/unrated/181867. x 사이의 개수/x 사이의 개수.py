def solution(myString):
    answer = []
    strings = myString.split('x')
    for i, string in enumerate(strings) :
        answer.append(len(strings[i]))
    return answer


def solution(myString) :
    return [len(x) for x in myString.split('x')] 