di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

### 입력
# 맵크기, 파이어볼 개수, 이동 명령 횟수
N, M, K = map(int, input().split())
# r, c, m, s, d = (r,c), 질량 m, 속력 s, 방향 d
fireball = [list(map(int, input().split())) for _ in range(M)]

# 턴 진행
for _ in range(K) :
    # [1] 개체별 이동
    for i in range(len(fireball)) :
        fireball[i][0] = (fireball[i][0] + di[fireball[i][4]] * fireball[i][3]) % N + 1
        fireball[i][1] = (fireball[i][1] + dj[fireball[i][4]] * fireball[i][3]) % N + 1

    # [2] 전체 개체 정렬 (좌표기준으로 정렬 => 같은 좌표 처리)
    fireball.sort(key=lambda x:(x[0], x[1]))
    fireball.append([100, 100, 0, 0, 0])        # 패딩: 마지막 요소 처리를 위한 인덱스
    new = []

    # [3] 같은 좌표 합치고 (2개 이상) + 나누고 (2개 이상) => new에 추가
    i = 0
    while i < len(fireball) - 1 :
        si, sj, m, s, d = fireball[i]       # 기준 좌표
        start = 0                           # 같으면 0, 2, 4, 6
        for j in range(i+1, len(fireball)) :
            if (si, sj) == (fireball[j][0], fireball[j][1]) :   # 같은 좌표
                m += fireball[j][2]
                s += fireball[j][3]
                if d%2 != fireball[j][4] % 2 :  # 다른 방향 start = 1
                    start = 1
            else :                          # 다른 좌표
                if j-i == 1:                # 1개 => 그냥 추가
                    new.append(fireball[i])
                else :                      # 여러개
                    if m//5 > 0 :           # 나눠도 1이상이면 (파이어볼이 살아있는 경우)
                        for dr in range(start, start+8, 2) :
                            new.append([si, sj, m//5, s//(j-i), dr])
                break
        i = j
    fireball = new

res = 0
for lst in fireball :
    res += lst[2]
print(res)