def gcd(a, b) :
    if b == 0 :
        return a
    if a % b == 0 :
        return b
    else :
        return gcd(b, a%b)
def sol_1711():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N) :
        check = dict()
        for j in range(N) :
            if i == j :
                continue

            x, y = points[i][0] - points[j][0], points[i][1] - points[j][1]
            val = gcd(x, y)
            x, y = x // val, y // val
            if (x,y) not in check :
                check[(x,y)] = 1
            else :
                check[(x, y)] += 1

        for nx, ny in check :
            if check.get((-ny, nx)) :
                ans += check[(nx, ny)] * check[(-ny, nx)]

    print(ans)

sol_1711()