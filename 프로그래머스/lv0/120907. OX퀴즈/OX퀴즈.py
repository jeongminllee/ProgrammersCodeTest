def solution(quiz):
    answer = []
    for i, q in enumerate(quiz) :
        if '=' in q :
            q = q.replace('=', '==')
            print(q)
            if eval(q) is True :
                answer.append('O')
            else :
                answer.append('X')
    return answer