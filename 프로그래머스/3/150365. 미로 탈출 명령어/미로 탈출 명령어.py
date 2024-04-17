import sys
sys.setrecursionlimit(10 ** 8)
# down, left, right, up 알파벳 순으로 정렬
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dAlpha = ['d', 'l', 'r', 'u']
answer = "z"    # 가능한 경로중 사전 순으로 가장 앞서는 경로를 저장. 초기값 z으로 설정하여 모든 문자열보다 뒤에 오도록 함

# isValid 함수는 주어진 위치가 n*m 격자 안에 있는지 확인
def isValid(nx, ny, n, m) :
    return 1 <= nx <= n and 1 <= ny <= m

# dfs함수는 깊이 우선 탐색을 통해 가능한 모든 경로를 찾는다.
def dfs(n, m, x, y, r, c, prev_s, cnt, k) :
    global answer
    # 현재 위치에서 목표 위치까지의 최소 이동 횟수보다 남은 이동 가능 횟수가 적을 경우 탐색 종료
    if k < cnt + abs(x - r) + abs(y - c) :
        return
    # 목표 위치에 도달했고 이동 횟수가 정확히 k일 때, 경로를 업데이트
    if x == r and y == c and cnt == k :
        answer = prev_s
        return
    # down, left, right, up  이동시도
    for i in range(4) :
        # 다음 위치가 유효하고 현재 경로가 지금까지의 최적해보다 사전순으로 앞서면 탐색 계속
        if isValid(x+dx[i], y+dy[i], n, m) and prev_s < answer :
            dfs(n, m, x+dx[i], y+dy[i], r, c, prev_s + dAlpha[i], cnt + 1, k)

def solution(n, m, x, y, r, c, k):
    # 맨해튼 거리 계산
    distance = abs(x - r) + abs(y - c)
    # 맨해튼 거리가 k보다 크거나, k와 거리의 차이가 홀수일 경우, 도착할 수 없으므로 
    if distance > k or (k - distance) % 2 == 1 :
        return "impossible"
    dfs(n, m, x, y, r, c, "", 0, k)
    return answer