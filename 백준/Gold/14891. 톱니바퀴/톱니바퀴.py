# 회전 top => 반시계 : top[i + 1]
# 회전시킬 후보 표시(idx, 오른쪽->, 왼쪽 <-), 회전
# => (톱니바퀴 번호, 같은 방향인지) % 2
# [1] idx 회전 후보 추가 tlst = [(idx, 0)]
# [2] 오른쪽 방향 처리 (극성이 같을 경우, break!)
#   for i (idx + 1, N + 1): # 일반화
# % 8      # 왼쪽    3시(+2) # 오른쪽 9시 (+6)
        # if arr[i - 1][(top[i - 1] + 2) % 8] != arr[i][(top[i] + 6)%8]
        # tlst.append((i, (i - idx)%2))
# [3] 왼쪽도 처리
# [4] for i, rot in tlst :
#       if rot == 0 :   # 같은 방향(dr)
#           top[i] = (top[i] - dr + 8) % 8
#       else :      (top[i] + dr) % 8

N = 4
arr = [[0] * 8] + [list(map(int, input())) for _ in range(N)]
K = int(input())
top = [0] * (N + 1)

for _ in range(K) :     # K 번 idx, dr 입력 받음 (회전 명령)
    idx, dr = map(int, input().split())
    # [1] idx 툽니를 회전
    tlst = [(idx, 0)]
    # [2] idx 우측 방향 처리(같은 극성 나오면 탈출)
    for i in range(idx + 1, N + 1) :
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전 후보 추가
        if arr[i - 1][(top[i - 1] + 2) % 8] != arr[i][(top[i] + 6) % 8] :
            tlst.append((i, (i - idx) % 2))
        else :              # 같은 극성이면 더 이상 전달 안 됨
            break

    # [3] idx 좌측 방향 처리(같은 극성 나오면 탈출)
    for i in range(idx - 1, 0, -1) :
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전 후보 추가
        if arr[i][(top[i] + 2) % 8] != arr[i + 1][(top[i + 1] + 6) % 8] :
            tlst.append((i, (idx - i) % 2))
        else :              # 같은 극성이면 더 이상 전달 안 됨
            break

    # [4] 실제 회전 처리 (cw 이면 top 값을 -1)
    for i, rot in tlst :
        if rot == 0 :       # idx 톱니의 dr과 같은 방향
            top[i] = (top[i] - dr + 8) % 8
        else :
            top[i] = (top[i] + dr + 8) % 8

# 점수 계산
ans = 0
tbl = [0, 1, 2, 4, 8]
for i in range(1, N + 1) :
    ans += arr[i][top[i]]*tbl[i]
print(ans)