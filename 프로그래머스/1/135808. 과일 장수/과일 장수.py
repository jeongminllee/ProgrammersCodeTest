def solution(k, m, score):
    answer = 0
    # 최대 이윤을 내기 위해 가장 가치가 높은 사과부터 판매한다.
    score.sort(reverse = True)
    # 반복문에 사용할 변수를 생성하고 초기화
    i = 0
    # 다음 상자에 사과를 포장할 수 있으면,
    while i + m <= len(score) :
        # 가장 비싼 사과부터 상자에 담는다.
        box = score[i : i + m]
        # 가격 책정 = 상자안에 가치가 가장 낮은 사과, 사과 갯수
        price = min(box) * len(box)
        # 정답에 더한다. 
        answer += price
        
        # 시작 포인트를 이동한다.
        i += m
        
    return answer