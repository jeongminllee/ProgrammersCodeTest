while 1 :
    N, M = map(int, input().split())
    if N == 0 and M == 0 :
        break
    arr1 = [int(input()) for _ in range(N)]
    arr2 = [int(input()) for _ in range(M)]
    cnt = 0
    for cd in arr2 :
        s, e = 0, N - 1
        while s <= e :
            mid = (s + e) // 2

            if arr1[mid] == cd :
                cnt += 1
                break
            elif arr1[mid] > cd :
                e = mid - 1
            elif arr1[mid] < cd :
                s = mid + 1
    print(cnt)