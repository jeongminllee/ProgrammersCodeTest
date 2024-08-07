# 출제 의도 : 비트 연산을 적절히 응용할 수 있는지
# f(x)는 다음과 같이 재해석될 수 있다. 
# => ......0 x + 1 - 0
# => .....01 x + 2 - 1
# => ....011 x + 4 - 2
# => ...0111 x + 8 - 4
# => ..01111 x + 16 - 8

# 먼저 x에 어떤 수를 더하는 행위는, 다르게 해석하면 x의 특정 비트 몇 개를 골라 반전시키는 행위로 해석할 수 있다.
# ex) 10 + 3은 10의 첫 3개의 비트를 반전시키는 것으로 해석할 수 있다.
# 여기서 우리는 x의 비트를 딱 하나 또는 두 개만 바꾸어야 합니다. 그러면서 동시에 x의 값을 이전보다 더 크게 키워야 함.
# 만약 x의 비트를 하나만 바꿀 경우, x는 커져야 하기 때문에 x의 어떤 0을 1로 바꿔야 하는데, 그렇다면 x가 가진 0 중에서 가장 낮은 위치에
# 있는 0을 1로 바꾸는 것이 이상적. x가 짝수인 경우가 바로 이 경우.

# 만약 x의 비트를 2개 바꿀 경우, 일단 하나의 0은 1로 바꿔야 하는데, 다른 하나는 그보다 좀 더 낮으면서 제일 높은 자리의 1을 0으로 바꾸는 것이 더 이상적.
# 왜냐하면, 비트는 윗자리로 갈수록 그 비트가 의미하는 값이 항상 커지기 때문에. x가 홀수인 경우가 바로 이 경우

# def solution(numbers):
#     return [num + ((num ^ (num + 1)) >> 2) + 1 for num in numbers]

# def solution(numbers):
#     answer = []
#     for n in numbers :
#         num = n
#         cnt = 0
#         while n % 2 == 1 :
#             cnt += 1
#             n //= 2
#         answer.append(num + 2**(cnt-1) if cnt != 0 else num+1)
#     return answer

def solution(numbers) :
    answer = []
    for num in numbers :
        if num % 2 == 0 :
            answer.append(num + 1)
        else :
            zero_bit = ((num ^ (num + 1)) >> 2) + 1
            answer.append(num + zero_bit)
    return answer