import sys
input = sys.stdin.readline

# 최대값 설정
MAX = 1000001

# DP 1 로 초기화
dp = [1] * MAX

# S: 값 누적 리스트
s = [0] * MAX

for i in range(2, MAX) :
    j = 1
    while i * j <= MAX - 1 :
        # 1의 배수에 값 추가
        dp[i*j] += i
        j += 1

for i in range(1, MAX) :
    # 누적 값 계산
    s[i] = s[i-1] + dp[i]

T = int(input())

res = []

for _ in range(T) :
    N = int(input())
    print(s[N])