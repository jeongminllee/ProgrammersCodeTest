def main() :
    n = int(input())
    arr = list(map(int, input().split()))

    total = 6 ** (4 - n)
    distinct = len(set(arr))

    if distinct < n :
        print(0, total)
        return

    r = 4 - n
    remaining = 6 - distinct

    ashley = 1
    for i in range(r) :
        ashley *= (remaining - i)

    brandon = total - ashley
    print(ashley, brandon)

if __name__ == "__main__" :
    main()