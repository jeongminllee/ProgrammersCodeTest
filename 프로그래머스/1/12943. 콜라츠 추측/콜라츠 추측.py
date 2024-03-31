def solution(num):
    answer = 0
    while num != 1 :
        if num % 2 == 0 :   # 짝수라면 2로 나눔
            num //= 2
        else :              # 홀수라면 3 * n + 1
            num = 3 * num + 1
        answer += 1         # 횟수 추가
        if answer >= 500 :  # 횟수가 500번 넘으면
            return -1       # -1 리턴
    return answer           # 500번 넘지 않으면 횟수 리턴