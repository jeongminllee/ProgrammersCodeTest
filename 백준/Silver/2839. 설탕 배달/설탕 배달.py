N = int(input())

def delivery(N) :
    cnt = 0
    while N >= 0 :
        if N % 5 == 0 :
            cnt += N // 5
            print(cnt)
            return
        N -= 3
        cnt += 1
    print(-1)

delivery(N)