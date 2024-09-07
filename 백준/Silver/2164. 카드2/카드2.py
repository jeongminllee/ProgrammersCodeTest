import math

def last_card(N) :
    # 1. N = 1의 경우를 제외
    if N == 1 :
        return 1
    # 3. 결과 값은 N보다는 작고 가장 큰 2*x를 N에서 뺀 후 2를 곱한 값
    power_of_two = 2 * (N - (2 ** math.floor(math.log2(N))))
    # 2. N = power_of_two 일 경우, 결과는 N
    return power_of_two if power_of_two != 0 else N

N = int(input())
print(last_card(N))


'''
N = 1: 1
N = 2: 2
N = 3: 2
N = 4: 4
N = 5: 2
N = 6: 4
N = 7: 6
N = 8: 8
N = 9: 2
N = 10: 4

1. N = 1 제외, 결과값은 항상 짝수
2. N이 2^n, 결과는 N 그 자체
3. 그 외의 경우, 결과는 N보다 작은 가장 큰 2^x 를 N에서 뺀 후 2를 곱한 값
'''