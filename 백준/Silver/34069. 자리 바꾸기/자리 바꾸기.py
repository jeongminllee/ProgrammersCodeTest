def main() :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    if N % 2 and M % 2 :
        print("No")
        return

    if N % 2 :
        for i in range(N) :
            for j in range(0,M,2) :
                tmp = arr[i][j]
                arr[i][j] = arr[i][j+1]
                arr[i][j+1] = tmp

    else :
        for i in range(0, N, 2) :
            for j in range(0,M) :
                tmp = arr[i][j]
                arr[i][j] = arr[i+1][j]
                arr[i+1][j] = tmp

    print("Yes")
    for a in arr :
        print(*a)

if __name__ == "__main__" :
    main()