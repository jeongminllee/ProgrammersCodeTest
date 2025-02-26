import sys
input = sys.stdin.readline

def sol_1711():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 모든 가능한 두 점의 조합에 대해
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                # 세 점의 좌표
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]

                # 세 변의 길이의 제곱 계산
                d1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
                d2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
                d3 = (x3 - x1) ** 2 + (y3 - y1) ** 2

                if 2 * max(d1, d2, d3) == d1 + d2 + d3 :
                    ans += 1

    print(ans)

sol_1711()