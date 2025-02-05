def main() :
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    tmp = [0, 0, 0]
    res = N * 1_000_000_007

    for i in range(N - 2) :
        a = i + 1
        b = N - 1

        while a < b :
            sol = arr[i] + arr[a] + arr[b]
            if abs(sol) < res :
                tmp = [arr[i], arr[a], arr[b]]
                res = abs(sol)

                if res == 0 :
                    break

            if sol < 0 :
                a += 1
            else :
                b -= 1
                
    print(*tmp)
    
main()