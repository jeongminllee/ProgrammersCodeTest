def main() :
    N, K = map(int, input().split())
    mod = 0
    res = []
    while mod < N :
        mod += 1
        if N % mod :
            continue
        res.append(mod)

    if len(res) < K :
        print(0)
        return
    else :
        print(res[K-1])
if __name__ == "__main__" :
    main()