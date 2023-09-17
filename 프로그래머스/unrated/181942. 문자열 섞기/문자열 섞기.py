def solution(str1, str2):
    answer = ''
    for s in range(len(str1)):
        answer = answer + str1[s] + str2[s]
    return answer