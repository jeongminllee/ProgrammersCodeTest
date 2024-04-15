def solution(e, starts):
    dp = [0] * (e + 1)
    dp_idx = [0] * (e + 1)

    for i in range(2, e+1) :
        for j in range(1, min(e//i + 1, i)) :
            dp[i*j] += 2
    for i in range(1, int(e**(1/2)) + 1) :
        dp[i**2] += 1

    cnt = 0
    for i in range(e, 0, -1) :
        if cnt <= dp[i] :
            cnt = dp[i]
            dp_idx[i] = i
        else :
            dp_idx[i] = dp_idx[i + 1]

    answer = []
    for s in starts :
        answer.append(dp_idx[s])

    return answer