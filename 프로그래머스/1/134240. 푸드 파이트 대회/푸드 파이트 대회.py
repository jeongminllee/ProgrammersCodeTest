def solution(food):
    # 음식을 담을 리스트
    food_str = []
    # food[0] = 물의 개수이기 때문에 무조건 1
    # food[1] 부터는 음식 갯수
    # 물 = 0, 음식 = 1부터 시작
    for i in range(1, len(food)) :
        # 음식은 최소 2개 이상이 있어야 배치 가능, 홀수면 나머지 1은 버림
        mid = food[i] // 2
        # 이를 리스트에 담음. 인덱스를 1/2 만큼을 담음 마지막에 양 극단으로 작성할 예정
        food_str.extend([str(i)] * mid)
    # 물의 인덱스는 0이기 때문에 가운데 두고 물을 기준으로 극단으로 갈수록 감소하는 str 작성
    answer = ''.join(food_str) + '0' + ''.join(reversed(food_str))
    
    return answer