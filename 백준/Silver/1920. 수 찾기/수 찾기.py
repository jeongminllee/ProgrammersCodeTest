import sys
input = sys.stdin.readline

N = int(input())
a = set(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

for j in b :
    if j in a :
        print(1)
    else :
        print(0)

# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# lst = list(map(int, input().split()))
# A.sort()
# 
# # 이분 탐색
# for num in lst :
#     lt, rt = 0, N - 1
#     isExist = False
# 
#     # 이분 탐색 시작
#     while lt <= rt :    # lt가 rt보다 커지면 반복문 탈출
#         mid = (lt + rt) // 2
#         if num == A[mid] :  # num(목표값)이 A[mid]값과 같다면 (목표값 존재여부를 알았다면)
#             isExist = True  # isExist True로 변경
#             print(1)        # 1 출력
#             break           # 반복문 탈출
#         elif num > A[mid] : # A[mid]가 num보다 작으면
#             lt = mid + 1    # lt를 높임
#         else :              # A[mid]가 num보다 높으면
#             rt = mid - 1    # rt를 낮춤

#     if not isExist :        # 찾지 못한 경우
#         print(0)            # 0 출력