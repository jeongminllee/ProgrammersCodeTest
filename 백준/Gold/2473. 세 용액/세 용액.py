def main() :
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    tmp = [0, 0, 0]
    res = N * 1_000_000_007

    for i in range(N - 2) :
        left = i + 1
        right = N - 1

        while left < right :
            sol = arr[i] + arr[left] + arr[right]
            if abs(sol) < res :
                tmp = [arr[i], arr[left], arr[right]]
                res = abs(sol)

                if res == 0 :
                    break

            if sol < 0 :
                left += 1
            else :
                right -= 1

    print(*tmp)

main()