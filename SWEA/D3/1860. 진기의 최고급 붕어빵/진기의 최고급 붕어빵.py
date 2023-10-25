T = int(input())
for test_case in range(1, T + 1) :
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.sort()

    ans = "Possible"
    cnt = 0
    for t in lst :
        cnt += 1
        if (t//M) * K < cnt :
            ans = "Impossible"

    print(f"#{test_case} {ans}")