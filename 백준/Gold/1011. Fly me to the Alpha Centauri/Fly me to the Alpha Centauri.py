import math
T = int(input())
for _ in range(T) :
    x, y = map(int, input().split())
    d = y - x
    if d <= 3 :
        print(d)
    else :
        n = int(math.sqrt(d))
        if d == n ** 2 :
            print(2 * n - 1)
        elif n ** 2 < d <= n * (n + 1) :
            print(2 * n)
        else :
            print(2 * n + 1)