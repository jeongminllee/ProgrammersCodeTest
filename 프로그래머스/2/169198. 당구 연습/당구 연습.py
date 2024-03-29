# 두 점 사이의 거리를 계산하는 함수
def distance(sX, sY, x, y):
    return (sX - x) ** 2 + (sY - y) ** 2

# 공의 위치를 반전시키는 함수. 벽에 부딫혔을 때의 반사를 모델링
def flip(m, n, x, y):
    return [
            (x, 2 * n - y),     # 상하 반전
            (2 * m - x, y),     # 좌우 반전
            (x, -y),            # 아래쪽 벽을 통해 반사
            (-x, y)             # 왼쪽 벽을 통해 반사
    ]

# 공이 시작 위치와 같은 선상에 있는지 판단하는 함수
def line(sX, sY, x, y):
    return [
        (sX == x and sY < y),   # 동일 세로선 상, 시작점 아래에 위치
        (sY == y and sX < x),   # 동일 가로선 상, 시작점 오른쪽에 위치
        (sX == x and sY > y),   # 동일 세로선 상, 시작점 위에 위치
        (sY == y and sX > x)    # 동일 가로선 상, 시작점 왼쪽에 위치
    ]

# 주어진 공의 위치들에 대해 시작 위치에서 각 공까지의 최소 거리를 계산하는 함수
def solution(m, n, startX, startY, balls):
    ans = []    # 결과
    for x, y in balls:  # 각 공의 위치에 대해 반복
        distances = (
            distance(startX, startY, *flip(m, n, x, y)[i])  # 반전된 위치에서의 거리를 계산
            for i in range(4)   # 네 가지 반전 경우에 대해
            if not line(startX, startY, x, y)[i]    # 공이 시작 위치와 같은 선상에 있지 않은 경우만 고려
        )
        ans.append(min(distances))  # 계산된 거리 중 최소값을 결과 리스트에 추가

    return ans  # 반환

# def solution(m, n, startX, startY, balls):
#     answer = []
    
#     for a, b in balls :
#         k = float('inf')
#         if startX != a or b > startY :
#             k = min(k, (startX - a) ** 2 + (startY + b) ** 2)
#         if startY != b or a > startX :
#             k = min(k, (startX + a) ** 2 + (startY - b) ** 2)
#         if startX != a or b < startY :
#             k = min(k, (startX - a) ** 2 + (2 * n - b - startY) ** 2)
#         if startY != b or a < startX :
#             k = min(k, (2 * m - a - startX) ** 2 + (startY - b) ** 2)
            
#         answer.append(k)
#     return answer