def solution(n, k):
    answer = []
    idx = 1
    while k * idx <= n :
        answer.append(k*idx)
        idx += 1
    return answer