def solution(n, k):
    answer = []
    idx = 1
    while k * idx <= n :
        answer.append(k*idx)
        idx += 1
    return answer

# def solution(n, k):
#     return [i for i in range(k,n+1,k)]
