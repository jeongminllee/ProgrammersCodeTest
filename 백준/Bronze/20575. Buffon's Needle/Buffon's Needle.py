def trunc(x) :
    if x >= 0 :
        return int(x)
    else :
        return -int(abs(x) + 1)
def main() :
    N = int(input())
    cnt = 0

    for _ in range(N) :
        x1, y1, x2, y2 = map(float, input().split())

        x1_trunc = trunc(x1)
        x2_trunc = trunc(x2)

        if abs(x1_trunc - x2_trunc) >= 1:
            cnt += 1

    pi = (2 / (cnt / N))

    print('{:.6f}'.format(pi))
    
main()