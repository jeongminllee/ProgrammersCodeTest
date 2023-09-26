def solution(my_string, n):
    answer = ''
    for i in my_string :
        answer += n * i
    return answer


def solution(my_string, n) :
    return ''.join(n * i for i in my_string)