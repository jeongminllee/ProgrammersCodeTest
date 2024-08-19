N, M = map(int, input().split())
named = [input().split() for _ in range(N)]
named.sort(key=lambda x: int(x[1]))

chars = [int(input()) for _ in range(M)]

for char in chars :
    left, right = 0, len(named)
    res = 0
    while left <= right :
        mid = (left + right) // 2
        if int(named[mid][1]) >= char :
            res = mid
            right = mid - 1
        else :
            left = mid + 1

    print(named[res][0])