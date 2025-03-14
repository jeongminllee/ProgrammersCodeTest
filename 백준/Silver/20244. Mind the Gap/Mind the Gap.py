def sol_20244() :
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.append(0)
    arr.sort()

    n = len(arr)

    max_d = 0
    min_d = 10**9 + 7

    for i in range(n) :
        if i + 1 < n :
            max_d = max(max_d, arr[i + 1] - arr[i])
        if i + 2 < n :
            min_d = min(min_d, arr[i + 2] - arr[i])

    if max_d >= min_d :
        print(0)
    else :
        print(max_d)
        

sol_20244()