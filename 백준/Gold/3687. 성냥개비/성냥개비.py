dp = [float('inf')] * 101   # dp테이블 생성
init_list = ['','',1,7,4,2,6,8] # 초기 리스트
for i in range(2, 8) :
    dp[i] = init_list[i]    # 2~7까지 초기값 입력 1 7 4 2 6 8

# 초기 리스트에선 '6'을 성냥 6개로 생성하였지만 첫번째 자리 이후에는 6은 '0'으로 생성
for i in range(8, 101) :
    for j in range(2, i-1) :
        dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i-j])))
        if j == 6 :
            dp[i] = min(dp[i], int(str(dp[i-j]) + '0'))

def find_biggest(num) : # 그리디
    res = '1' * (num // 2)  # 1이 성냥 2개가 들기 떄문에 num // 2 만큼 1을 생성
    if num % 2 :
        res = '7' + res[1:] # 홀수이면 7을 가장 앞에 붙인 후, 1을 num // 2 - 1 만큼 생성
    return res

def find_smallist(num) :
    return dp[num]

T = int(input())
for _ in range(T) :
    n = int(input())    # 성냥개비의 개수
    print(find_smallist(n), find_biggest(n))

'''
큰 수와 작은 수를 구할 때 다른 방식으로 접근

큰 수를 구하는 것은 그리디 알고리즘을 이용
성냥의 개수가 짝수라면 1111..., 홀수라면 711111...

작은 수는 DP로 접근.
1자리 숫자로 사용되는 최대 성냥 개수는 7이므로, 2부터 7까지를 가장 작은 숫자 1 7 4 2 6 8 로 초기화
DP[i]를 i개의 성냥으로 만들 수 있는 가장 작은 수라고 할 때, 임의의 j(2<=j<=i-2)에 대해
DP[i] = min(DP[i], concat(DP[i-j], DP[j]))
여기서 주의해야 할 점은, DP[6] = 6으로 초기화하였으나 이후 연산에서 뒤에서 concat시에는 0으로 취급되어야 한다.
숫자는 0으로 시작할 수 없기 때문에 초기값을 두번째로 작은 값인 6으로 초기화되었기 때문이다.
'''