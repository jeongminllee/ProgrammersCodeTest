N, D = map(int, input().split())
buildings = list(map(int, input().split()))

dct = {}
for b in buildings :
    try :
        dct[b] += 1
    except :
        dct[b] = 1

mx = max(dct.keys())

res = 0
for _ in range(D) :
    if mx == 0 :
        break
    res += dct[mx]
    try :
        dct[mx-1] += dct[mx]
    except :
        dct[mx-1] = dct[mx]

    mx -= 1

print(res)