T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # lst = list(map(int, input().split()))

    # ans = s = 0
    # while s<N:
    #     i_max = s
    #     for i in range(s+1, N):
    #         if lst[i_max] < lst[i]:
    #             i_max = i
    #     for i in range(s, i_max):
    #         ans += (lst[i_max] - lst[i])
    #     s = i_max + 1

    lst = list(map(int, input().split()))
    ans = mx = 0
    for n in lst[::-1]:
        if mx < n:
            mx = n
        else:
            ans += (mx - n)

    print(f'#{test_case} {ans}')