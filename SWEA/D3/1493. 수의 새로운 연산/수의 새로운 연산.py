dct = {}
r_dct = {}
i, j = 1, 1
for n in range(1, 50000) : # 10000까지의 숫자를 좌표에 저장할 때, 그 4배의 크기의 삼각형
    dct[n] = (i, j)
    r_dct[(i, j)] = n
    i, j = i - 1, j + 1
    if i < 1 :
        i, j = j, 1
T = int(input())
for test_case in range(1, T + 1) :
    p, q = map(int, input().split())

    pi, pj = dct[p] # [1] p, q 값의 좌표로 전환
    qi, qj = dct[q]

    ans = r_dct[(pi + qi, pj + qj)]          # [2] 좌표를 값으로 변환
    print(f"#{test_case} {ans}")