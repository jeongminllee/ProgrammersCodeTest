def F(a, b, c):
    return ((b**2) // (4*a)) + c

def sol_10325() :
    n = int(input())    # the number of gears in the engine
    lst = []
    for _ in range(n) :
        a, b, c = map(int, input().split())
        lst.append((a, b, c))

    if n == 1 :
        print(1)
        return

    ans = 0   # very higher value
    res = 0
    for i, (a, b, c) in enumerate(lst) :
        if ans < F(a, b, c) :
            ans = max(ans, F(a, b, c))
            res = i

    print(res + 1)
    return

T = int(input())
for _ in range(T) :
    sol_10325()