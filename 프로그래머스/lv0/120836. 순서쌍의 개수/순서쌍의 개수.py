def solution(n):
    answer = 0
    ans = [i for i in range(1, n + 1)]
    for i in ans :
        if n % i == 0 :
            answer += ans[0]
    return answer