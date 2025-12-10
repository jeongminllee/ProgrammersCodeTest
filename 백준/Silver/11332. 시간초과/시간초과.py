MOD = 10**8

def O_N(N, max_ops) :
    return N <= max_ops

def O_N2(N, max_ops) :
    return N**2 <= max_ops

def O_N3(N, max_ops) :
    return N**3 <= max_ops

def O_2N(N, max_ops) :
    val = 1
    for _ in range(N) :
        val <<= 1
        if val > max_ops :
            return False
    return True

def O_fact(N, max_ops) :
    val = 1
    for i in range(1, N+1) :
        val *= i
        if val > max_ops :
            return False
    return True


C = int(input())
time_complex = list(input().split() for _ in range(C))

# S, N, T, L
# 시간 복잡도, 입력의 최대범위, 테스트 케이스의 수, 제한시간

for S, N, T, L in time_complex :
    N, T, L = int(N), int(T), int(L)

    max_ops = (MOD * L) // T
    if S == "O(N)" :
        res = O_N(N, max_ops)

    elif S == "O(N^2)" :
        res = O_N2(N, max_ops)

    elif S == "O(N^3)" :
        res = O_N3(N, max_ops)

    elif S == "O(2^N)" :
        res = O_2N(N, max_ops)

    else :  # O(N!)
        res = O_fact(N, max_ops)

    if res is False :
        print("TLE!")
    else :
        print("May Pass.")