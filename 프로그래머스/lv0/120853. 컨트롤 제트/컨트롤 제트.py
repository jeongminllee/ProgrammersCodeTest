# def solution(s):
#     answer = 0
#     string = s.split(' ')
#     for i, num in enumerate(string) :
#         if num == 'Z' :
#             string[i] = '-' + string[i - 1]
#             if '--' in string[i]:
#                 string[i] = string[i].replace('--', '')

#     for a in string :
#         answer += int(a)
#     return answer

def solution(s) :
    answer = []
    for i in s.split() :
        if i != 'Z' :
            answer.append(int(i))
        else :
            answer.pop()
    return sum(answer)