P = int(input())
for _ in range(P) :
    T, *lst = map(int, input().split())
    cnt = 0
    for i in range(1, 20) :
        for j in range(i) :
            if lst[i] < lst[j] :
                cnt += 1
    print(f"{T} {cnt}")