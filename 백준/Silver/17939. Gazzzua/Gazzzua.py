def sol_17939() :
    N = int(input())
    arr = list(map(int, input().split()))

    max_price = arr[-1]
    res = 0

    for i in range(N-1, -1, -1) :
        if arr[i] > max_price :
            max_price = arr[i]
        else :
            res += max_price - arr[i]
    
    print(res)
    
sol_17939()