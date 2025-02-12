def main() :
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    for i in range(1, M + 1) :
        for j in range(1, N) :
            if arr[j-1] % i > arr[j] % i :
                arr[j-1], arr[j] = arr[j], arr[j-1]

    for a in arr :
        print(a)

main()