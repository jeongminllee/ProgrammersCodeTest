def sol_3211() :
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr.sort()

    res = 1

    while res <= N and arr[res - 1] + 1 > res :
        res = arr[res - 1] + 1

    print(res)

sol_3211()