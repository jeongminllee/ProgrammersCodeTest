def dfs(now:int, visited:int) -> int :
    # 정답처리
    if visited == bit_range - 1 :
        if arr[now][0] != 0 :
            return arr[now][0]
        else :
            return INF

    # 이미 구한 구간이면 메모이제이션
    if (now, visited) in dp :
        return dp[(now, visited)]

    # 탐색 및 최소 시간 구하기
    min_cost = INF
    for i in range(N) :
        if arr[now][i] == 0 :
            continue
        if visited & (1<<i) == 0 :
            min_cost = min(dfs(i, (visited | 1<<i)) + arr[now][i], min_cost)
    dp[(now, visited)] = min_cost
    return min_cost

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

INF = 1<<32
bit_range = 1 << N
dp = {} # DP 테이블을 딕셔너리 형태로 사용

print(dfs(0, 1))