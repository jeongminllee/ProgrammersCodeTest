def check(n) :
    if n == 1 :
        return False
    
    for i in range(2, int(n ** (1/2)) + 1) :
        if n % i == 0 :
            return False
    return True

M, N = map(int, input().split())
for n in range(M, N + 1) :
    if check(n) :
        print(n)