N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0     # 변수를 생성할 때는 위치/초기값 고민 후 작성
for i in range(N - 2) :
    for j in range(i + 1, N - 1) :
        for k in range(j + 1, N) :
            if ans < lst[i] + lst[j] + lst[k] <= M :
                ans = lst[i] + lst[j] + lst[k]

print(ans)