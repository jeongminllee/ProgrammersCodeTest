import sys
input = sys.stdin.readline

def char_to_index(c) :
    return ord(c) - ord('a')

def is_valid(encrypted, original) :
    n, m = len(encrypted), len(original)

    # 원래 비밀번호와 첫 윈도우에 대한 빈도수를 저장할 배열 (알파벳 26개)
    target_freq = [0] * 26
    window_freq = [0] * 26

    for c in original :
        target_freq[char_to_index(c)] += 1

    # 첫 m개의 문자에 대한 윈도우 빈도수 계산
    for i in range(m) :
        window_freq[char_to_index(encrypted[i])] += 1

    # 초기 윈도우 체크
    if window_freq == target_freq :
        return True

    # 슬라이딩 윈도우 : 오른쪽으로 한 칸씩 이동하면서 빈도수 업데이트
    for i in range(m, n) :
        # 새로 들어오는 문자 업데이트
        window_freq[char_to_index(encrypted[i])] += 1
        # 윈도우에서 벗어나는 문자 업데이트
        window_freq[char_to_index(encrypted[i - m])] -= 1

        if window_freq == target_freq :
            return True

    return False

def sol_9549() :
    encrypted = input().rstrip()
    original = input().rstrip()
    print('YES' if is_valid(encrypted, original) else 'NO')

T = int(input())
for _ in range(T) :
    sol_9549()