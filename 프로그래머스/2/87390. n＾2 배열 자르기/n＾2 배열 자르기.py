# def solution(n, left, right):
#     return [max(i % n, i // n) + 1 for i in range(left, right + 1)]
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1) :
        answer.append(max(i % n , i // n) + 1)
        
    return answer