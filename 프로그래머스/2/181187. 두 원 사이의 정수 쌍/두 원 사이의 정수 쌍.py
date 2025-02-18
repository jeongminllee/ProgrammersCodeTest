from math import sqrt, floor, ceil
# math.sqrt = 루트
# math.floor = 내림
# math.ceil = 올림

def solution(r1, r2):
    answer = 0  # 격자점의 총 수를 저장할 변수 초기화
    for i in range(1, r2 + 1):  # 1부터 r2까지 반복 (원의 1/4 부분에 대해 계산)

        if i < r1:  # i가 r1보다 작은 경우, 즉, 내부 원의 범위 안에 있을 때
            # r2 원의 x=i에서의 y값 최댓값의 바닥값과
            # r1 원의 x=i에서의 y값 최솟값의 천장값 사이의 격자점 수를 계산
            answer += floor(sqrt(r2 ** 2 - i ** 2)) - ceil(sqrt(r1 ** 2 - i ** 2)) + 1
        else:  # i가 r1보다 크거나 같은 경우, 즉, 내부 원이 없는 영역에서
            # r2 원의 x=i에서의 y값 최댓값의 바닥값까지의 격자점 수를 계산
            answer += floor(sqrt(r2 ** 2 - i ** 2)) + 1
            
    return answer * 4