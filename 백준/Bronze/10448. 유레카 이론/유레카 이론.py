T = int(input())
for _ in range(T) :
    n = int(input())
    tbl = [0]
    a = 1
    t = 0
    while t < 1000 :
        t = (a*(a+1))//2
        tbl.append(t)
        a += 1

    res = False
    for i in tbl[1:] :
        for j in tbl[1:] :
            for k in tbl[1:] :
                if n == (i + j + k) :
                    res = True
                    break

    print(int(res))