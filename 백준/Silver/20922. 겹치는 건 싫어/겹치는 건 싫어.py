N, K = map(int, input().split())
lst = list(map(int, input().split()))
a, b = 0, 0

cnt = [0] * (max(lst) + 1)
ans = 0

while b < N :
    if cnt[lst[b]] < K :
        cnt[lst[b]] += 1
        b += 1
    else :
        cnt[lst[a]] -= 1
        a += 1

    ans = max(ans, b - a)
print(ans)