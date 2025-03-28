def sol_5600() :
    a, b, c = map(int, input().split())
    N = int(input())
    res = [2] * (a + b + c + 1)

    check = []

    for _ in range(N) :
        i, j, k, r = map(int, input().split())

        if r == 1 :
            res[i] = res[j] = res[k] = 1
        else :
            check.append((i, j, k))

    for i, j, k in check :
        if res[i] == 1 and res[j] == 1 :
            res[k] = 0
        elif res[i] == 1 and res[k] == 1 :
            res[j] = 0
        elif res[j] == 1 and res[k] == 1 :
            res[i] = 0

    for ans in res[1:] :
        print(ans)
        
sol_5600()