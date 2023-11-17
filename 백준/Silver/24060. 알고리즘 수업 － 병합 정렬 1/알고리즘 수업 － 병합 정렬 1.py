def find(start, end) :
    global K
    if start== end :
        return 
    mid = (start + end) // 2
    find(start, mid) ; find(mid + 1, end)
    if K <= end - start + 1 :
        j = sorted(arr[start : end + 1])
        print(j[K - 1]) ; exit()
    
    K -= end - start + 1

N, K = map(int, input().split())
arr = list(map(int, input().split()))
find(0, N - 1) ; print(-1)