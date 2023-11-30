N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
l, r = min(lst), sum(lst)
while l <= r :
    m = (l + r ) // 2
    money = m
    draw = 1
    
    for i in lst :
        if money < i :
            money = m
            draw += 1
        money -= i
        
    if draw > M or m < max(lst) :
        l = m + 1
    else :
        r = m - 1
        k = m
        
print(k)