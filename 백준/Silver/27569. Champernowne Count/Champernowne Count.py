def main() :
    n, k = map(int, input().split())
    num = cnt = 0
    for i in range(1, n + 1) :
        num = (num * (10 ** len(str(i))) + i) % k
        if num % k == 0 :
            cnt += 1
    print(cnt)
main()