from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj) :
    q = deque()
    q.append((si, sj))
    # 시작 방문 표시
    visited[si][sj] = 1
    # 시작 위치 개수 세기
    cnt = 1

    # BFS
    while q :
        ci, cj = q.popleft()
        # 현재 그룹에 포함
        zeros[ci][cj] = group

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]

            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and not arr[ni][nj] :
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1

    return cnt

# 이동할 수 있는 총 그룹의 개수를 세는 함수
def move_cnt(ci, cj) :
    # 그룹 번호를 담기 위한 집합 생성
    data = set()

    for d in range(4) :
        ni, nj = ci + di[d], cj + dj[d]

        if 0 <= ni < n and 0 <= nj < m and zeros[ni][nj]:
            data.add(zeros[ni][nj])

    # 현재 ci, cj 위치 세기
    cnt = 1

    # 갈 수 있는 모든 그룹에 대하여 한 그룹씩 받으면서
    for c in data :
        # info에 추가
        cnt += info[c]
        # 이동할 수 있는 칸의 개수를 10으로 나눈 나머지 계산
        cnt %= 10

    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

# 방문 표시
visited = [[0] * m for _ in range(n)]
# 그룹 번호를 알려주는 2차원 배열
zeros = [[0] * m for _ in range(n)]
# 결과 값 표시
ans = [[0] * m for _ in range(n)]

# grouping
group = 1
# {그룹명, 그룹 안에 포함된 총 개수} 딕셔너리 생성
info = {}

for i in range(n) :
    for j in range(m) :
        # 이동할 수 있고 아직 방문하지 않은 위치라면
        if not arr[i][j] and not visited[i][j] :
            # 현재 위치에서 이동할 수 있는 0의 개수 세기
            cnt = bfs(i, j)
            # 딕셔너리에 그룹명과 개수 추가
            info[group] = cnt
            # 다음 그룹
            group += 1

# 전체 데이터를 하나씩 살펴보며
for i in range(n) :
    for j in range(m) :
        # 벽이 있다면
        if arr[i][j] :
            # 벽을 부수고 인접해 있는 그룹의 총 개수 받기
            ans[i][j] = move_cnt(i, j)

# 정답 출력
for i in range(n) :
    print(''.join(map(str, ans[i])))
