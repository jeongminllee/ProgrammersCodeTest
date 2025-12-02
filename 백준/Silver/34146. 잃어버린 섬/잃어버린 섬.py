def main() :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dct = {}

    for i in range(N) :
        for j in range(M) :
            if arr[i][j] not in dct :
                dct[arr[i][j]] = 0
            dct[arr[i][j]] += 1

    if M % 2 == 0 :
        for val in dct.values() :
            if val % 2 :
                print("NO")
                return

    else :
        cnt = sum(1 for v in dct.values() if v % 2 == 1)

        if not (cnt <= N and (cnt % 2 == N % 2)) :
            print("NO")
            return

    print("YES")
if __name__ == "__main__" :
    main()