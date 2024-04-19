import copy
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

arr = [list(input().rstrip()) for _ in range(10)]
v = [[0] * 10 for _ in range(10)]

ans = float('inf')

for i in range(10) :
    for j in range(10) :
        if arr[i][j] == "O" :
            v[i][j] = 1

# 첫 번째 줄의 모든 경우의 수
for ck in range(1 << 10) :
    visitied = copy.deepcopy(v)
    cnt = 0
    # 첫 줄에 10개 전구 하나씩 탐색
    for k in range(10) :
        # j번째 스위치를 누른다면 +1
        if ck & (1 << k) :
            cnt += 1
            # 맨 윗줄 전구 살피기
            for d in range(5) :
                nx, ny = 0 + dx[d], k + dy[d]
                if 0 <= nx < 10 and 0 <= ny < 10 :
                    visitied[nx][ny] = not visitied[nx][ny]

    for x in range(1, 10) :
        for y in range(10) :
            if visitied[x-1][y] == 1 :
                cnt += 1
                for d in range(5) :
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < 10 and 0 <= ny < 10 :
                        visitied[nx][ny] = not visitied[nx][ny]

    if all(c == 0 for c in visitied[-1]) :
        ans = min(ans, cnt)
print(ans if ans < 101 else -1)