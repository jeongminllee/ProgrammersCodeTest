def is_prime(num) :
    if num == 1 :
        return False

    for i in range(2, int(num ** (1/2)) + 1) :
        if num % i == 0 :
            return False

    return True

M = int(input())
N = int(input())
sm = 0
mn = 10000

for num in range(M, N+1) :
    if is_prime(num) :
        sm += num
        mn = min(num, mn)

if sm == 0 :
    print(-1)
else :
    print(sm)
    print(mn)