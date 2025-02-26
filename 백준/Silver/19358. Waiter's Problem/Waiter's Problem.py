def sol_19358() :
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    ans = 0
    for i in range(n) :
        tip = lst[i]
        ans += max(0, tip - i)
    print(ans)
    
T = int(input())
for _ in range(T) :
    sol_19358()