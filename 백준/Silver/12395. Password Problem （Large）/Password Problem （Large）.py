def sol_12395() :
    A, B = map(int, input().split())
    already_key = list(map(float, input().split()))
    p = [1.0]

    for i in range(A) :
        p.append(p[-1] * already_key[i])
    
    res = 1 << 32

    for k in range(A + 1) :
        cnt = k + (B - A + k + 1) + (1-p[A-k]) * (B + 1) 

        res = min(res, cnt)

    res = min(res, 1 + B + 1)

    return res

T = int(input())
for t in range(1, T + 1) :
    print(f"Case #{t}: {sol_12395():.6f}")