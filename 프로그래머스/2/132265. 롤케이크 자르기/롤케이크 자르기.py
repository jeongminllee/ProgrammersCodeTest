from collections import Counter

# topping 배열을 입력으로 받아서, 피자를 나눌 수 있는 경우의 수를 반환하는 함수
def solution(topping):
    split_cnt = 0  # 피자를 나눌 수 있는 경우의 수를 저장할 변수
    topping_cnt = Counter(topping)  # 각 토핑의 개수를 계산하여 저장
    half_topping_set = set()  # 현재까지 고려된 토핑의 종류를 저장할 집합
    
    # 피자 토핑 배열을 순회
    for t in topping:
        half_topping_set.add(t)  # 현재 토핑을 집합에 추가
        topping_cnt[t] -= 1  # 현재 토핑의 개수를 하나 줄임

        if topping_cnt[t] == 0:  # 만약 현재 토핑의 개수가 0이 되면,
            topping_cnt.pop(t)  # 해당 토핑을 카운터에서 제거

        # 왼쪽 부분(현재까지 고려된 토핑의 종류)과 오른쪽 부분(나머지 토핑의 종류)의 토핑 종류 수가 같다면
        if len(half_topping_set) == len(topping_cnt):
            split_cnt += 1  # 나눌 수 있는 경우의 수를 하나 증가시킴
            
    return split_cnt  # 나눌 수 있는 경우의 수 반환
