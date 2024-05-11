def solution(temperature, t1, t2, a, b, onboard):
    # 초기값 설정
    cost = 1000 * 100       # 최댓값 설정(onboard 길이 최댓값 * a,b 최댓값)
    t1 += 10                # 음수를 제거하기 위해 -10 <= t1, t2 <= 40 을 0 <= t1, t2 <= 50 으로 옮긴다
    t2 += 10
    temperature += 10       # t1, t2 도 옮겼으니 temprature 도 + 10 을 해준다

    # DP[i][j] : i분에 j 온도를 만들 수 있는 가장 적은 전력
    dp = [[cost] * 51 for _ in range(len(onboard))]  # j = 0 ~ 50
    dp[0][temperature] = 0

    flag = 1  # 에어컨을 가동했을때 온도가 변하는 방향, 최적의 온도보다 낮거나 같으면
    if temperature > t2:
        flag = -1   # 최적의 온도보다 외부 온도가 높다면

    for i in range(1, len(onboard)):
        start = end = 0

        if onboard[i] :
            start = t1
            end = t2
        else :
            start = min(t1, temperature)
            end = max(t2, temperature)

        for j in range(start, end+1):
            ans = [cost]
            if (onboard[i] == 1 and t1 <= j <= t2) or onboard[i] == 0:
                # 1. 에어컨을 키지 않고 실외온도와 달라서 실내온도가 -flag 되는 경우
                if 0 <= j + flag <= 50:
                    ans.append(dp[i - 1][j + flag]) # 에어컨 off
                # 2. 에어컨을 키지 않고 현재온도 j 가 실외온도랑 같아서 변하지 않는 경우
                if j == temperature:
                    ans.append(dp[i - 1][j])        # 에어컨 off
                # 3. 에어컨을 키고 현재온도가 변하는 경우
                if 0 <= j - flag <= 50:
                    ans.append(dp[i - 1][j - flag] + a) # 에어컨 on
                # 4. 에어컨을 키고 현재온도가 희망온도라서 온도가 변하지 않는경우
                if t1 <= j <= t2:
                    ans.append(dp[i - 1][j] + b)        # 에어컨 on

                dp[i][j] = min(ans)         # 최소 소비 전력 구하기

    answer = min(dp[len(onboard) - 1])      # return
    return answer