def solution(quiz):
    answer = []
    for i, q in enumerate(quiz) :
        L, R = q.split('=')
        a, op, b = L.split()
        if op == '+' :
            ans = 'O' if bool(int(a) + int(b) == int(R)) else 'X'
            answer.append(ans)
        elif op == '-':
            ans = 'O' if bool(int(a) - int(b) == int(R)) else 'X'
            answer.append(ans)
        
    return answer