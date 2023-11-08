T = int(input())

cnt = 0

if T % 5 == 0 :
    print(T // 5)
else :
    cnt = 0
    while T > 0 :
        T -= 3
        cnt += 1
        if T % 5 == 0 :
            cnt += T // 5
            print(cnt)
            break
        elif T == 1 or T == 2 :
            print(-1)
            break
        elif T == 0 :
            print(cnt)
            break