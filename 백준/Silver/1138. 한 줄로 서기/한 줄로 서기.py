N = int(input())
lst = list(map(int, input().split()))
ans = [0] * N

for i in range(N) :
    cnt = 0
    for j in range(N) :
        if ans[j] == 0 :
            if cnt == lst[i] :
                ans[j] = i + 1
                break
            cnt += 1
print(*ans)