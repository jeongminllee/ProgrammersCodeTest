H, W = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

for i in range(1, W-1) :
    left = max(lst[:i])
    right = max(lst[i+1:])
    compare = min(left, right)

    if lst[i] < compare :
        ans += compare - lst[i]

print(ans)