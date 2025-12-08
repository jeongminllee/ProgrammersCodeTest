def main() :
    S = int(input())
    v = [0] * 26
    res = ""
    for _ in range(S) :
        char = input().strip().replace(" ", "")
        for c in char :
            idx = ord(c) - ord("A")
            if v[idx] :
                continue
            v[idx] = 1
            res += c
    print(res)

if __name__ == "__main__" :
    main()