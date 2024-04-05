while 1 :
    N, M = map(int, input().split())
    if N == 0 and M == 0 :
        break
    dic = {}
    cnt = 0
    for _ in range(N) :
        cd = int(input())
        dic[cd] = 1

    for _ in range(M) :
        cd = int(input())
        if cd in dic :
            cnt += 1
    print(cnt)