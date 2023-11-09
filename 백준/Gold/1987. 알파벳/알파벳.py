import sys
from collections import deque
input = sys.stdin.readline

def dfs(ci, cj, cnt) :
    global ans
    ans = max(ans, cnt)

    # 4방향, 범위 내, 중복값 아님
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
        ni, nj = ci + di, cj + dj
        if 0 <= ni < R and 0 <= nj < C and v[ord(arr[ni][nj])] == 0 :
            v[ord(arr[ni][nj])] = 1
            dfs(ni, nj, cnt + 1)
            v[ord(arr[ni][nj])] = 0


def bfs() :
    # q 등 필요 데이터 생성
    q = deque()
    # v = [[[] for _ in range(C)] for _ in range(R)]  # 리스트는 O(N)
    v = [[set() for _ in range(C)] for _ in range(R)]  # set는 O(1)
    ans = 1
    # q에 초기데이터(들) 삽입
    q.append((0, 0, arr[0][0]))
    v[0][0].add(arr[0][0])            # set이면 add, list 면 append

    while q:
        ci, cj, cv =q.popleft()
        ans = max(ans, len(cv))
        # 4방향, 범위 내, 중복값 아님, 중복 시퀀스 아닌 경우
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] not in cv:
                if cv + arr[ni][nj] not in v[ni][nj] :
                    q.append((ni, nj, cv+arr[ni][nj]))
                    v[ni][nj].add((cv+arr[ni][nj])) # set이면 add, list 면 append

    return ans

R, C = map(int, input().split())
arr = list(input() for _ in range(R))

# ans = 1
# v = [0] * 128   # 아스키코드
# v[ord(arr[0][0])] = 1   # 해당 값을 사용했음(방문표시)
# dfs(0, 0, 1)
ans = bfs()
print(ans)

