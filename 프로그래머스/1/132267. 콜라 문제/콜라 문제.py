def solution(a, b, n):
    answer = 0
    # 콜라를 바꿀 수 있는 갯수동안
    while n >= a :
        # 빈 콜라병을 가져다 주면 얼만큼 바꿔주는지 계산
        val = (n // a) * b
        # answer에 더함
        answer += val
        # 총 콜라병을 다시 계산
        n = val + n % a
    # 바꿔온 콜라병 갯수를 return => 총 마신 콜라 갯수 아님
    return answer