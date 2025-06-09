INF = 1 << 32

def sol_16306(n) :
    res = INF

    i = 1
    while i ** 3 <= n :
        if n % i != 0 :
            i += 1
            continue

        n_div_i = n // i
        j = i
        while j * j <= n_div_i :
            if n_div_i % j != 0 :
                j += 1
                continue

            k = n_div_i // j
            surface_area = 2 * (i*j + j*k + k*i)
            res = min(res, surface_area)
            j += 1
        i += 1
    return res

n = int(input())

print(sol_16306(n))