def main() :
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    left = 0
    res = 10 ** 9
    for i in range(n-1) :
        left += arr[i]
        right = total - left

        diff = abs(left - right)

        res = min(res, diff)

    print(res)

if __name__ == "__main__" :
    main()