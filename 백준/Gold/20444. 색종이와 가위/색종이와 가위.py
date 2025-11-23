def main() :
    n, k = map(int, input().split())
    left = 0
    right = n // 2

    while left <= right :
        rowCut = (left + right) // 2
        colCut = n - rowCut

        pieces = (rowCut + 1) * (colCut + 1)
        if k == pieces :
            print('YES')
            return

        if k > pieces :
            left = rowCut + 1
        else :
            right = rowCut - 1

    print("NO")

if __name__ == "__main__" :
    main()