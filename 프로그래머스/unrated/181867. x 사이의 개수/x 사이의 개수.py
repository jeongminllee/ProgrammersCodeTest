def solution(myString):
    answer = []
    strings = myString.split('x')
    for i, string in enumerate(strings) :
        answer.append(len(strings[i]))
    return answer