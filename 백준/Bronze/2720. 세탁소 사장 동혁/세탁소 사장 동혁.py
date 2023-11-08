T = int(input())

for _ in range(T) :
    N = int(input())
    q, q_div=divmod(N, 25)
    d, d_div=divmod(q_div, 10)
    n, n_div=divmod(d_div, 5)
    p, p_div=divmod(n_div, 1)

    print(q, d, n, p)