def solution(n, k):
    answer = []
    a = 0
    b = 0
    while b < n :
        a += 1
        b = k * a
        if b > n :
            break
        answer.append(b)
    return answer