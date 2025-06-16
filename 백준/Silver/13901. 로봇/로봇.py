# 방 크기
R, C = map(int, input().split())

# 방 설정
arr = [[0] * C for _ in range(R)]

# 장애물 설치
K = int(input())
for _ in range(K) :
    br, bc = map(int, input().split())
    arr[br][bc] = 1

# 로봇 초기 설정
sr, sc = map(int, input().split())
arr[sr][sc] = 1

# 방향 입력
direction = list(map(int, input().split()))

# 방향 설정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 로봇 현재 위치
cr, cc = sr, sc

# 로봇이 더 이상 움직이지 않을 때 까지 반복
while True :
    moved = False   # 이번 턴에 이동 여부 확인

    for dir in direction :  # 이동 시도
        while True :
            nr, nc = cr + dr[dir - 1], cc + dc[dir - 1] # 다음 방향 이동 시도

            # 방문 가능한지
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0 :
                moved = True
                arr[nr][nc] = 1
                cr, cc = nr, nc

            # 만약 불가능하면 중단
            else :
                break
    # 만약 한 번도 이동하지 못했다면 종료
    if not moved :
        break

# 최종 위치 출력
print(cr, cc)