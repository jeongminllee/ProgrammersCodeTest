N, K = map(int, input().split())
lst = list(map(int, input().split()))
robot = [0]*N

ans = cnt = 0
while True :
    ans += 1
    # [1] 벨트, 로봇 회전 + [N-1]로봇 내림
    # lst = [lst[-1]] + lst[:-1]  # 364ms
    # robot = [0] + robot[:-1]
    # robot[N-1] = 0

    lst.insert(0,lst.pop()) # 268ms
    robot.pop()
    robot.insert(0,0)
    robot[N-1] = 0

    # [2] 먼저 올라간 로봇부터 처리
    for i in range(N-2, 0, -1) :
        if robot[i] == 1 and robot[i+1]==0 and lst[i+1] > 0 :
            robot[i], robot[i+1] = 0, 1
            lst[i+1] -= 1    # 내구도가 감소해서 0이 되면 cnt += 1

            if lst[i+1] == 0 :
                cnt += 1

    # [3] 0자리 내구도 > 0 이면 로봇 올림
    if lst[0] > 0 :
        robot[0] = 1
        lst[0] -= 1

        if lst[0] == 0:
            cnt += 1

    # [4] 0인 개수 >= K 이면 탈출
    # if lst.count(0) >= K :      # 268ms 매번 0의 개수를 카운트 : 느리다..
    #     break
    if cnt >= K :
        break

print(ans)