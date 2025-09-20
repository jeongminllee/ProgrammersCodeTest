N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 257

for i in range(N) :
    for j in range(M) :
        cnt[arr[i][j]] += 1

best_time = 10**19
best_h = 0

for h in range(257) :
    time = 0
    curr = B

    for k in range(257) :
        c = cnt[k]
        if c == 0 :
            continue
        if k < h :
            need = (h - k) * c
            curr -= need
            time += need
        elif k > h :
            rem = (k - h) * c
            curr += rem
            time += 2 * rem


    if curr >= 0 and time <= best_time :
        best_time = time
        best_h = h

print(best_time, best_h)