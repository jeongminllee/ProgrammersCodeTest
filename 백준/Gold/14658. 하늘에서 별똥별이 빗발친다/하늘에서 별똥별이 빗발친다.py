N, M, L, K = map(int, input().split())
arr = []
ans = 0
for _ in range(K) :
    x, y = map(int, input().split())
    arr.append((x, y))
    
for i in range(K) :
    for j in range(K) :
        cnt = 0
        
        sx, sy = min(arr[i][0], arr[j][0]), min(arr[i][1], arr[j][1])

        for x, y in arr :
            if sx <= x <= sx + L and sy <= y <= sy + L :
                cnt += 1

        ans = max(ans, cnt)
        
res = K - ans
print(res)