import sys
input = sys.stdin.readline

N = int(input())                        # 탭의 개수
lst = []  # 각 탭의 길이
sm_lst = [0]
for _ in range(N) :
    num = int(input())
    lst.append(num)
    sm_lst.append(sm_lst[-1] + num)

L = int(input())                        # 화면 길이
Q = int(input())                        # 탭 클릭 횟수

for _ in range(Q) :
    tap = int(input()) - 1
    total_dist = min(sm_lst[tap] + lst[tap]/2 - L/2, sm_lst[-1] - L)
    pos = max(0, total_dist)
    print(f'{pos:.2f}')