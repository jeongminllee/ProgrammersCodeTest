def div_sum(num) :
    res = 0

    while num > 0 :
        res += num % 10
        num //= 10

    return res

lst = []
while True :
    N = int(input())
    if N == 0 :
        break

    ans = div_sum(N)

    for p in range(11, 1<<32 + 1) :
        number = N * p
        res = div_sum(number)
        if res == ans :
            print(p)
            break