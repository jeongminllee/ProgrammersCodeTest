def mobius(n) :
    """n에 대한 뫼비우스 함수 값을 반환"""
    if n == 1 :
        return 1
    # 소인수 분해 진행
    prime_cnt = 0
    i = 2
    tmp = n
    while i * i <= tmp :
        if tmp % i == 0 :
            prime_cnt += 1

            if tmp // i % i == 0 :
                return 0
            while tmp % i == 0 :
                tmp //= i
        i += 1
    if tmp > 1 :
        prime_cnt += 1
    return -1 if prime_cnt % 2 else 1

def sol_18255() :
    N = int(input())
    total = 0
    for d in range(1, N + 1) :
        cnt = (N // d + 1) ** 3 - 1
        total += mobius(d) * cnt

    print(total)

T = int(input())
for _ in range(T) :
    sol_18255()