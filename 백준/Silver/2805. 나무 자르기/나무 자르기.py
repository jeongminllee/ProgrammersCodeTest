N, M = map(int, input().split())
lst = list(map(int, input().split()))
s = 1
e = max(lst)

while s <= e :
    mid = (s + e) // 2

    ans = 0
    for i in lst :
        if i >= mid :
            ans += i - mid

    if ans >= M :
        s = mid + 1
    else :
        e = mid - 1
        
print(e)