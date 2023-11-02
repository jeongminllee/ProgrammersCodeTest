def count(arr) :
    ret = 0
    for lst in arr :
        cnt = 0
        for j in range(len(lst)) :
            if lst[j] :    # 값이 0이 아닌 경우
                cnt += 1
            else :
                if cnt == K :
                    ret += 1
                cnt = 0

    return ret

T = int(input())

for test_case in range(1, T + 1) :
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr) + count(arr_t)


    print(f"#{test_case} {ans}")