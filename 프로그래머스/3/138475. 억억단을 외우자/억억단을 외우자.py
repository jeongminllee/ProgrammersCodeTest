def solution(e, starts):
    # dp는 각 숫자의 약수의 개수를 저장
    # dp_idx는 해당 인덱스까지의 수 중 가장 많은 약수를 가진 수를 저장
    dp = [0] * (e + 1)
    dp_idx = [0] * (e + 1)

    # 2부터 e까지 모든 수에 대해
    for i in range(2, e+1) :
        # i의 배수에 대해 약수의 개수를 증가
        for j in range(1, min(e//i + 1, i)) :
            dp[i*j] += 2
    # 1부터 e의 제곱근까지 모든 정수 i에 대해
    for i in range(1, int(e**(1/2)) + 1) :
        # i의 제곱은 약수의 개수를 1 증가 시킴
        dp[i**2] += 1
    
    cnt = 0     # 가장 많은 약수를 가진 수
    # e부터 1까지 역순으로 탐색
    for i in range(e, 0, -1) :
        # 현재 숫자의 약수 개수가 현재까지 발견된 최대 약수 개수보다 많거나 같으면
        if cnt <= dp[i] :
            cnt = dp[i]     # 갱신
            dp_idx[i] = i   # 갱신
        # 현재 숫자보다 더 많은 약수를 가진 수가 이미 발견되었다면, 해당 수를 dp_idx에 저장
        else :
            dp_idx[i] = dp_idx[i + 1]
    
    answer = []
    
    for s in starts :
        # 약수 개수를 answer 배열에 추가
        answer.append(dp_idx[s])

    return answer