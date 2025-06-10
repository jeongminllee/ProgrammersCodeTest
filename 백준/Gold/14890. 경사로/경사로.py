def check(lst, v) :
    cnt = 1         # 연속된 동일 숫자의 개수 카운트
    for i in range(1, len(lst)) :
        if lst[i-1] == lst[i] :         # 같은 경우
            cnt += 1
        # 1 증가된 경우 => 경사로를 놓을 수 있는지 체크
        # 1 증가되었고, 연속된 길이가 L이상이고, 겹쳐서 놓지 않은 경우
        elif lst[i-1] + 1 == lst[i] and cnt >= L and v[i-L:i] == [0] * L :
            cnt = 1                     # 카운트 다시 시작
            v[i-L:i] = [1] * L          # 사용표시

        elif lst[i-1] > lst[i] :        # 내려가는 경우 => 반대방향에서 고민
            cnt = 1
        else :                          # 2 이상 올라가는 경우 => 불가능
            return False
    return True

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 전치행렬로 열 => 행 처리, 양방향 처리로(역방향도 처리)
res = 0
for _ in range(2) :         # 전치행렬 처리
    for lst in arr :
        v = [0] * len(lst)  # 미방문 (겹쳐서 놓지 않기 위해)
        # 증가방향도 성공 and 감소방향(반대방향)도 성공이면
        if check(lst, v) and check(lst[::-1], v[::-1]) :
            res += 1

    # 열의 행처리를 위해서 전치행렬로 변환
    arr = list(map(list, zip(*arr)))
print(res)