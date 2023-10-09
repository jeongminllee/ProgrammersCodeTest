def solution(i, j, k):
    answer = 0
    for a in range(i, j + 1) :
        a = str(a)
        if str(k) in a :
            answer += a.count(str(k))
    return answer