def sol_7453() :
    n = int(input())
    res = 0
    A, B, C, D = [], [], [], []

    for _ in range(n) :
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    dct = {}
    for a in A:
        for b in B :
            v = a + b
            if v not in dct :
                dct[v] = 1
            else :
                dct[v] += 1

    for c in C :
        for d in D :
            v = -(c + d)
            if v in dct :
                res += dct[v]
    print(res)


sol_7453()