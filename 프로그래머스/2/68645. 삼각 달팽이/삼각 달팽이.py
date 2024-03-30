# 비유/파이썬/챌린저
steps = (
    # l : length, d : depth
    lambda l, d : (u + d for u in range(l)),
    lambda l, d : (1,) * l,
    lambda l, d : (u - d for u in range(-(l + 2), -2))
)

def fill_side(arr, idx, num, length, direction, depth) :
    direction %= 3
    for step in steps[direction](length, depth) :
        idx += step
        num += 1
        arr[idx] = num

    if direction == 2 :
        depth += 2

    # 그 다음에 실행될 fill_side 함수의 args
    return arr, idx, num, length - 1, direction + 1, depth

def solution(n):
    answer = [0] * sum(range(n + 1))
    args = (answer, 0, 0, n, 0, 0)

    # recursion error 방지를 위해 반복문으로 실행
    while args[3] > 0 :
        args = fill_side(*args)

    return answer

# def solution(n):
#     answer = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]    # 삼각형 구조 만들기

#     x, y = -1, 0    # 좌표 초기화 => 처음 시작은 아래로 내려가기 때문에 x = -1
#     num = 1

#     for i in range(n) : # 방향
#         for j in range(i, n) :  # 좌표 구하기
#             if i % 3 == 0 : # 하
#                 x +=1
#             elif i % 3 == 1 :   # 우
#                 y += 1
#             else :  # 상
#                 x -= 1
#                 y -= 1
#             answer[x][y] = num
#             num += 1

#     return sum(answer, [])

# answer = 삼각형 배열
# x, y = 좌표 값
# num = 대입 숫자
# i = 방향값
# j = i방향에 대한 대입 횟수