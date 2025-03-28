def sol_16826() :
    power = input().rstrip()
    cnt = 0
    tmp = 0
    for p in power :
        if p == 'R' :
            tmp += 1
            if tmp == 4 :
                cnt += 1
                tmp = 0
        else :
            tmp -= 1
            if tmp % 4 == 0 :
                tmp = 0

    print(cnt)

sol_16826()