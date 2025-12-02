def main() :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    best = 0
    for i in range(M) :
        for j in range(i+1, M) :
            for k in range(j+1, M) :
                total = 0
                for a in range(N) :
                    total += max(arr[a][i], arr[a][j], arr[a][k])
                best = max(best, total)

    print(best)


if __name__ == "__main__" :
    main()