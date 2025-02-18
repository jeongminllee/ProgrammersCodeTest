import sys
input = sys.stdin.readline

# T = -aR^2 + bR + c    1 <= a,b,c <= 10,000
# 변곡점을 구하는 문제
# a = 양수이기 때문에 (-a = 음수)최대 지점을 구하는 문제.
# 기울기 = -2aR + b
# 변곡점은 기울기가 0
# -2aR + b = 0
# R = b / 2a 지점이 변곡점 => 여기서는 최고점이 될 것이다.
# T = -a * (b / 2a) ^ 2 + b * (b / 2a) + c
# = (- b^2 / 4a) + (b^2 / 2a) + c
# = b^2 / 4a + c
# F(a, b, c) = b^2 / 4a + c

def F(a, b, c) :
    return ((b**2) / (4*a)) + c
def sol_10325() :
    n = int(input())
    torque = [list(map(int, input().split())) for _ in range(n)]
    if n == 1 :
        print(1)
        return

    # ans = 수식의 답
    # gear_num = 몇번째 기어인지
    ans = gear_num = 0

    for i, (a, b, c) in enumerate(torque, 1) :
        if ans < F(a, b, c) :
            ans = F(a, b, c)
            gear_num = i

    print(gear_num)
    return

T = int(input())
for _ in range(T) :
    sol_10325()