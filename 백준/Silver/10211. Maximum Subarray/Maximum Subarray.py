T = int(input())
for _ in range(T) :
    N = int(input())
    lst = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]

    # 2차원 배열인 이유는 시작 지점을 찾는거임. 일단 구현해보고 더 좋은 방법 찾자
    res = lst[0]
    curr = lst[0]

    for i in range(1, N) :
        curr = max(lst[i], curr + lst[i])
        res = max(res, curr)
    print(res)