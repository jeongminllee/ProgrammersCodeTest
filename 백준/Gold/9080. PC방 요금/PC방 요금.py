def main() :
    hm, spd = input().split()
    hh, mm = map(int, hm.split(':'))
    spd = int(spd)

    ans = 0
    hh = (hh + 2) % 24  # 밤 10시 - 아침 8시 에서 00시 - 10시로 시간 이동시킴

    while spd > 0 :
        # 야간 정액 구간이 00:00 - 10:00
        # 이때 야간 정액을 쓰기 유리한 시점이 00:00 ~ 04:00에 해당되는 조건
        # spd > 300 : 5시간 이상 사용을 해야 이득임.
        if hh <= 4 and spd > 300 :
            spd -= (600 - (hh * 60 + mm))
            hh = 10
            mm = 0
            ans += 5000

        else :
            hh = (hh + 1) % 24  # 1시간 이용    
            spd -= 60           # 1시간 이용
            ans += 1000         # 요금 지불

    print(ans)

T = int(input())
for _ in range(T) :
    main()