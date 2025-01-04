def mod(N) :
    r = 999999999
    x = 0

    while r :
        if 9 < (N // r) :
            return -1
        x = (x + N // r) * 10
        N %= r
        r //= 10

    return x

def test() :
    N = int(input())
    if N % 9 != 0 :
        return -1
    return mod(N)

T = int(input())
res = []
for _ in range(T) :
    res.append(test())
print(' '.join(map(str, res)))