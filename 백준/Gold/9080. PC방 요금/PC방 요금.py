def solve():
    # 입력 형식: "HH:MM D"
    time_str, d_str = input().split()
    D = int(d_str)
    HH, MM = map(int, time_str.split(":"))
    # 시작 시각을 0분부터의 절대 분으로 계산 (예: 00:00 → 0, 14:30 → 14*60+30)
    start = HH * 60 + MM
    end = start + D  # 세션 종료 시각(절대 분)

    memo = {}  # dp 메모이제이션

    # 현재 시각 x(절대 분)가 야간 요금 적용 시간에 해당하는지?
    # 야간 시간은 밤10시(22:00, 1320분)부터 자정 그리고 자정부터 아침 08:00(480분)까지.
    def is_night(x):
        r = x % 1440
        return (r >= 1320 or r < 480)

    # x가 야간 구간에 있다면, 야간 정액은 “밤10시부터 다음날 아침 08시까지” (또는
    # 자정 이후라면 당일 08:00까지) 커버합니다.
    def night_end(x):
        r = x % 1440
        if r >= 1320:
            return (x // 1440 + 1) * 1440 + 480
        elif r < 480:
            return (x // 1440) * 1440 + 480
        else:
            # 이 함수는 x가 야간 구간일 때만 호출됩니다.
            return x

    # f(x): 현재 절대 시각 x부터 세션 종료(end)까지의 최소 비용
    def f(x):
        if x >= end:
            return 0
        if x in memo:
            return memo[x]
        best = float('inf')
        # 일반 요금 옵션:
        # x부터 어떤 y까지 일반 요금을 쓰면 비용은 1000 * ceil((y-x)/60)
        # 단, 구간이 길어질수록 비용이 동일한 "계단" 구간이 있으므로,
        # 구간의 끝 후보는
        #   1. x에서 60분씩 더한 시각 (즉, x+k*60)
        #   2. 세션 종료 시각 end
        #   3. 야간 정액 전환을 위해 중요한 시각 (밤10:00, 아침 08:00)
        # 를 고려합니다.
        cand = set()
        # (1) x+k*60 (x+k*60 <= end)
        max_k = (end - x) // 60
        for k in range(1, max_k + 1):
            cand.add(x + k * 60)
        # (2) 세션 종료 시각
        cand.add(end)
        # (3) x와 end 사이에 위치한 밤 10시(22:00)나 아침 08:00(08:00) 시각
        #    전환 시각은 절대 시각으로 d*1440+480, d*1440+1320 (d: day) 입니다.
        start_day = (x // 1440) - 1
        end_day = (end // 1440) + 1
        for d in range(start_day, end_day + 1):
            for boundary in (d * 1440 + 480, d * 1440 + 1320):
                if x < boundary <= end:
                    cand.add(boundary)
        # 각 후보 y에 대해 구간 [x, y]를 일반 요금으로 처리하는 비용 + f(y)를 고려
        for y in sorted(cand):
            seg = y - x
            cost_seg = 1000 * ((seg + 59) // 60)  # ceil(seg/60)와 같음.
            candidate = cost_seg + f(y)
            if candidate < best:
                best = candidate

        # 야간 정액 옵션:
        # 만약 현재 x가 야간 시간대라면, 5000원을 내면
        #   - 세션 종료(end)가 야간 구간의 끝(N)보다 이전이면 5000원으로 끝내고,
        #   - 아니면 5000원 + f(N) (N: night_end(x))
        # 를 고려할 수 있습니다.
        if is_night(x):
            N = night_end(x)
            if end <= N:
                candidate = 5000
            else:
                candidate = 5000 + f(N)
            if candidate < best:
                best = candidate

        memo[x] = best
        return best

    ans = f(start)
    print(ans)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T) :
        solve()