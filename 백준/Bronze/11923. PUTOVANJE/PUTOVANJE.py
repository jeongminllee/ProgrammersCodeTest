N, C = map(int, input().split())
fruits = list(map(int, input().split()))

max_cnt = 0

for start in range(N) :
    total = 0
    cnt = 0

    for i in range(start, N) :
        if total + fruits[i] <= C :
            total += fruits[i]
            cnt += 1

    max_cnt = max(cnt, max_cnt)

print(max_cnt)