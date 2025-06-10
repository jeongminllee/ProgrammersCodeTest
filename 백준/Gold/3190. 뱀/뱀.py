N = int(input())
K = int(input())
apple = [tuple(map(int, input().split())) for _ in range(K)]

L = int(input())
dlst = [input().split() for _ in range(L)]

dtbl = [0] * 10001          # 방향 전환에 사용되는 룩업테이블 생성
for sec, turn in dlst :
    dtbl[int(sec)] = turn

di, dj = [-1,0,1,0], [0,1,0,-1]  # 시계방향으로 방향정의
dr = 1                              # 오른쪽 방향
snake = [(1, 1)]                    # 좌측상단
res = 0                             # 0초

while True :
    res += 1                        # 1초 경과
    ci, cj = snake[0]               # 현재 머리 좌표
    ni, nj = ci + di[dr], cj + dj[dr]   # 진행방향으로 한 칸 이동
    # 벽에 부딪혔거나, 뱀 몸에 부딪힌 경우 종료
    if 1 <= ni <= N and 1 <= nj <= N and (ni, nj) not in snake :
        snake.insert(0, (ni,nj))    # 머리 위치[0]에 이동좌표 확장
        if (ni, nj) in apple :
            apple.remove((ni, nj))
        else :
            snake.remove((snake[-1]))       # 꼬리부분 제거\
        # 방향전환
        if dtbl[res] == 'D' :       # 우회전 명령
            dr = (dr + 1) % 4
        elif dtbl[res] == 'L' :     # 좌회전 명령
            dr = (dr + 3) % 4
    else :          # 종료
        break
print(res)