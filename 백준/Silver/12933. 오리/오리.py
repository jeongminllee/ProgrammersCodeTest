def main() :
    S = list(input())
    res = 0

    if S[0] != 'q' or S[-1] != 'k' or len(S) % 5 :
        print(-1)
        return

    def find_uack(start) :
        nonlocal res
        quack = "quack"
        j = 0
        new_ori = True

        for i in range(start, len(S)) :
            if S[i] == quack[j] :
                if S[i] == 'k' :
                    if new_ori :
                        res += 1
                        new_ori = False
                    j = 0
                    S[i] = 0
                    continue
                j += 1
                S[i] = 0

    for i in range(len(S) - 4) :
        if S[i] == 'q' :
            find_uack(i)

    if any(S) or res == 0 :
        print(-1)
    else :
        print(res)

if __name__ == "__main__" :
    main()