def solution(X, Y):
    # X와 Y에 있는 각 숫자의 개수를 세기 위한 딕셔너리
    cnt_X = {str(i) : 0 for i in range(10)}
    cnt_Y = {str(i) : 0 for i in range(10)}

    # X와 Y의 각 숫자의 개수를 세어 cnt_X, cnt_Y에 기록
    for x in X :
        cnt_X[x] += 1
    for y in Y :
        cnt_Y[y] += 1

    # 짝꿍을 문자열로 만들기
    answer = ''
    for i in range(9, -1, -1) : # 가장 큰 수부터 시작해야 하므로 거꾸로 반복
        # X와 Y에 공통적으로 존재하는 숫자의 개수를 찾아 그 개수만큼 answer에 추가
        cnt = min(cnt_X[str(i)], cnt_Y[str(i)])
        answer += str(i) * cnt

    # 짝궁이 없거나 0으로만 구성되어 있을 경우를 처리
    if not answer :
        return "-1"
    elif set(answer) == {"0"}:
        return "0"
    else :
        return answer
