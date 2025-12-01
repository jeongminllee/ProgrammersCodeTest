def main() :
    t = int(input())

    for _ in range(t) :
        S = input()
        res = ''
        for i in range(len(S)) :
            if S[i] == '-' :
                continue
            elif S[i].isdigit() :
                res += S[i]
            elif S[i].isalpha() :
                if S[i] in "ABC" :
                    res += "2"
                elif S[i] in "DEF" :
                    res += "3"
                elif S[i] in "GHI" :
                    res += "4"
                elif S[i] in "JKL" :
                    res += "5"
                elif S[i] in "MNO" :
                    res += "6"
                elif S[i] in "PQRS" :
                    res += "7"
                elif S[i] in "TUV" :
                    res += "8"
                else : # "WXYZ"
                    res += "9"
        res = res[:10]

        ans = ''
        for i in range(len(res)) :
            if i == 3 or i == 6 :
                ans += "-"
            ans += res[i]

        print(ans)

if __name__ == "__main__" :
    main()