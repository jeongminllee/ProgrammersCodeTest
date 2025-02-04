def main() :
    def f(w, x) :
        cnt = 0

        while w > x :
            if w % 2 == 0 :
                m = w // 2
            else :
                m = w // 2 + 1

            cnt += 1

            if m <= x :
                return cnt
            w = m

        return cnt


    W, H, A = map(int, input().split())

    answer = float('inf')
    for x in range(1, min(W, A) + 1) :
        if A % x == 0 :
            y = A // x

            if y <= H :
                cnt = f(W, x) + f(H, y)

                answer = min(answer, cnt)

    if answer == float('inf') :
        print(-1)
    else :
        print(answer)

main()