# N : 층수, K : 디스플레이에 나타나는 층 자리 수, P : 반전시킬 수, X : 실제 멈춰있는 층
N, K, P, X = map(int, input().split())
nums = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2], # 0 to n
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], # 1 to n
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3], # 2 to n
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], # 3 to n
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], # 4 to n
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1], # 5 to n
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], # 6 to n
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], # 7 to n
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1], # 8 to n
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]  # 9 to n
]

ans = 0
for target in range(1, N+1) :
    now = X
    cnt = 0
    for _ in range(K) :
        cnt += nums[now % 10][target % 10]
        now //= 10
        target //= 10

    if 1 <= cnt <= P :
        ans += 1

print(ans)