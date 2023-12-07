T = int(input())

for _ in range(T) :
    k = int(input())
    n = int(input())
    k0 = [i for i in range(1, n + 1)]
    for f in range(k) :
        for j in range(1, n) :
            k0[j] += k0[j - 1]
    print(k0[-1])
