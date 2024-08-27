def equation(sm, sign, num, n, string) :
    if n == N :
        sm += sign * num
        if sm == 0 :
            print(string)
    else :
        equation(sm, sign, num * 10 + (n + 1), n + 1, string + ' ' + str(n + 1))
        equation(sm+sign*num, 1, (n + 1), n + 1, string + '+' + str(n + 1))
        equation(sm+sign*num, -1, (n + 1), n + 1, string + '-' + str(n + 1))

T = int(input())
for _ in range(T) :
    N = int(input())
    equation(0, 1, 1, 1, '1')
    print()