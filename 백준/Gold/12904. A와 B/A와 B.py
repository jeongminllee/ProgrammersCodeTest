def main() :
    S = list(input())
    T = list(input())

    while T :
        if T[-1] == 'A' :
            T.pop()
        elif T[-1] == 'B' :
            T.pop()
            T.reverse()

        if S == T :
            print(1)
            return
    print(0)


if __name__ == "__main__" :
    main()