def can_attach(arr, x, y, size) :
    if x + size > 10 or y + size > 10 :
        return False

    for i in range(x, x + size) :
        for j in range(y, y + size) :
            if arr[i][j] != 1 :
                return False

    return True

def attach(arr, x, y, size, value) :
    for i in range(x, x + size) :
        for j in range(y, y + size) :
            arr[i][j] = value

def solve(arr, paper_cnt, x, y, cnt) :
    global ans

    # 이미 찾은 최소값보다 큰 경우 탐색 중단
    if cnt >= ans :
        return

    # 마지막 행까지 도달한 경우
    if x >= 10 :
        ans = min(ans, cnt)
        return

    # 다음 행으로 이동
    if y >= 10 :
        solve(arr, paper_cnt, x + 1, 0, cnt)
        return

    # 현재 위치가 0이거나 이미 덮인 경우
    if arr[x][y] != 1 :
        solve(arr, paper_cnt, x, y + 1, cnt)
        return

    # 각 크기의 색종이를 시도
    for size in range(5, 0, -1) :
        if paper_cnt[size] > 0 and can_attach(arr, x, y, size) :
            paper_cnt[size] -= 1
            attach(arr, x, y, size, 0)  # 색종이 부착

            solve(arr, paper_cnt, x, y + size, cnt + 1)

            paper_cnt[size] += 1
            attach(arr, x, y, size, 1)  # 색종이 제거

arr = [list(map(int, input().split())) for _ in range(10)]

# 각 크기별 색종이 개수 (인덱스 1부터 5까지 사용)
paper_cnt = [0, 5, 5, 5, 5, 5]

# 답을 저장할 변수 (최소값을 찾기 위해 큰 값으로 초기화)
ans = float('inf')

# 백트래킹 시작
solve(arr, paper_cnt, 0, 0, 0)

# 결과 출력
print(-1 if ans == float('inf') else ans)