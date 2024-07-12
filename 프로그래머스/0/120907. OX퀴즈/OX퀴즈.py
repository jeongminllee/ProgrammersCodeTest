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

# def solution(quiz):
#     answer = []

#     for i, q in enumerate(quiz) :
#         func, res = q.split(' = ')
#         func = func.replace(' - ', ' + -').split(' + ')
#         if sum(int(num) for num in func) == int(res) :
#             answer.append("O")
#         else :
#             answer.append("X")

#     return answer