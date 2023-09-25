def solution(myString, pat):
    answer = 0
    for i, x in enumerate(myString) :
        if myString[i:].startswith(pat) :
            answer += 1
    return answer
