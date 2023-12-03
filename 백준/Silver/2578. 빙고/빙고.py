arr = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 숫자: lst (1차원으로 생성/저장)
lst = []
for _ in range(5) :
    lst += list(map(int, input().split()))

# 번호마다 좌표의 위치를 저장
pos_lst = [0] * 26

for i in range(5) :
    for j in range(5) :
        pos_lst[arr[i][j]] = (i, j)

v = [[0] * 10 for _ in range(4)]    # v0~v3 빈도수 체크
# 사회자가 부르는 좌표를 읽어서, 빈도수 체크, 5인 개수가 3개 이상이면 종료
for n in lst :
    i, j = pos_lst[n]           # 번호에서 좌표를 읽어옴
    v[0][j] += 1                # 세로(열) 위치를 누적
    v[1][i] += 1                # 가로(행) 위치를 누적
    v[2][i - j] += 1            # 우측 아래 대각선 개수를 누적
    v[3][i + j] += 1            # 우측 위쪽 대각선 개수를 누적
    cnt = 0
    for tmp in v :
        cnt += tmp.count(5)     # 5개 인 개수(한줄 완성된 개수)

    if cnt >= 3 :               # 줄이 3개 이상이면 빙고!
        break
print(sum(v[0]))                # 표시(누적)된 개수가 불러준 숫자의 개수