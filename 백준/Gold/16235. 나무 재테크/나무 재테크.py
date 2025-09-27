di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

# 입력 및 초기상태
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]   # 추가할 양분
A = [[5] * N for _ in range(N)] # 초기상태

woods = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M) :
    x, y, z = map(int,input().split())
    woods[x-1][y-1].append(z)

### 입력 및 초기상태 끝

for year in range(K) :
    # [1] 봄: 자신의 나이만큼 양분을 먹고 나이가 1 증가.
    # 1*1 크기의 칸에 있는 양분만 먹을 수 있음.
    # 하나의 칸에 여러 그루의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
    # 만약, 땅에 있는 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 죽는다.

    for i in range(N) :
        for j in range(N) :
            woods[i][j].sort()                      # 어린 순으로 정렬
            for k in range(len(woods[i][j])) :    # 순서대로 처리
                if woods[i][j][k] <= A[i][j] :
                    A[i][j] -= woods[i][j][k]     # 양분 흡수
                    woods[i][j][k] += 1
    # [2] 여름 : 죽은 나무가 양분이 된다. 죽은 나무는 나이//2 양분으로 추가된다.
                else :                              # 양분 없는 경우
                    while k < len(woods[i][j]) :    # 나머지 나무는 양분으로
                        A[i][j] += (woods[i][j].pop()//2)
                    break

    # [3] 가을 : 나무 번식, BFS로 8방향, 범위내, 미방문...은 필요가 있나?,
    for i in range(N) :
        for j in range(N) :
            for k in range(len(woods[i][j])) :
                if woods[i][j][k]%5 == 0 :      # 나이가 5의 배수인 경우
                    for d in range(8) :
                        ni, nj = i + di[d], j + dj[d]
                        if 0<=ni<N and 0<=nj<N :
                            woods[ni][nj].append(1)

    # print(f'{year + 1} autumn : {woods}')
    ### 가을 끝

    # [4] 겨울 : A 를 추가로 더한다.
    for i in range(N) :
        for j in range(N) :
            A[i][j] += arr[i][j]
    ### 겨울 끝

res = 0
for i in range(N) :
    for j in range(N) :
        res += len(woods[i][j])

print(res)