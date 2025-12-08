def main() :
    N = int(input())
    left = 1
    right = N

    res = []

    while left < right :
        res.append(left)
        res.append(right)
        left += 1
        right -= 1

    if left == right :
        res.append(left)

    print(*res)

if __name__ == "__main__" :
    main()