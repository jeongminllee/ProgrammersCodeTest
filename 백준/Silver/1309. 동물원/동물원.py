N = int(input())
# a = 사자를 배치하지 않을 경우의 수, b = 사자를 배치하는 모든 경우의 수
a, b = 1, 3

for i in range(1, N) :
    # 위 수식을 보면 dp[i][1]과 dp[i][2]는 왼쪽, 오른쪽만 다른, 동일한 수식임을 알 수 있다.
    # 그래서 b*2를 해주고 비어있는 경우의수 a를 더해준다.
    # 이때 a는 직전에 사자를 배치하는 모든 경우의 수의 합이 된다. 
    # 이번에 배치하지 않을 것이기 떄문에 모든 경우의 수를 더한 경우의 수를 가질 수 있다.
    a, b = b, (a + b * 2) % 9901

print(b)