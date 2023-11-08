T = int(input())

for _ in range(T) :
    N = int(input())
    q, N=divmod(N, 25)
    d, N=divmod(N, 10)
    n, N=divmod(N, 5)
    p = N

    print(q, d, n, p)