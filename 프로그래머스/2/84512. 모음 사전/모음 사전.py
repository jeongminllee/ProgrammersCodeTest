# 각 자리수마다 가능한 경우의 수는 다음과 같습니다.
#
# 첫 번째 자리: 'A', 'E', 'I', 'O', 'U' (5가지)
# 두 번째 자리: 'AA', 'AE', 'AI', 'AO', 'AU', 'EA', 'EE', ... , 'UU' (5^2가지)
# 세 번째 자리: 'AAA', 'AAE', 'AAI', ... , 'UUU' (5^3가지)
# 네 번째 자리: 'AAAA', 'AAAE', 'AAAI', ... , 'UUUU' (5^4가지)
# 다섯 번째 자리: 'AAAAA', 'AAAAE', 'AAAAI', ... , 'UUUUU' (5^5가지)
# 각 자리수가 증가할 때마다 그 자리에 올 수 있는 경우의 수는 5의 거듭제곱만큼 증가
# 따라서, 각 자리수를 기준으로 해당 자리수 이전의 모든 경우의 수를 더해준다.

# "AAAE" 의 경우
# A = 1
# AA = 1 + 5 = 6
# AAA = 1 + 5 + 25 = 31
# AAAE = 1 + 5 + 25 + 125 + 4 = 31 + 125 + 4 = 160
def solution(word):
    answer = 0
    n = len(word)
    for i, char in enumerate(word) :
        # 'A', 'E', 'I', 'O', 'U' 순서대로 0, 1, 2, 3, 4로 매핑
        value = 'AEIOU'.index(char)
        # 각 자리수마다 5의 거듭제곱을 곱해줌.
        # 자리수가 낮을수록 더 큰 값
        answer += value * (5 ** (4 - i))
        # 현재 자리수 이전의 모든 경우의 수를 합산
        for j in range(4 - i) :
            answer += (5 ** j) * value

    return answer + n   # 단어 길이를 더해줌 (각 단어의 시작을 1로 카운팅)