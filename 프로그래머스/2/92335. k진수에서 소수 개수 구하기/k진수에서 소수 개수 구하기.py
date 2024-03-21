def solution(n, k) :
    word = ''
    # n을 k진수로 변환
    while n :
        word = str(n % k) + word
        n //= k

    # k진수로 변환된 문자열에서 '0'을 기준으로 나누어 리스트를 만듦
    word = word.split('0')

    # 리스트의 각 요소에 대해 소수인지 아닌지 검사
    cnt = 0
    for w in word :
        if len(w) == 0 :
            continue
        if int(w) < 2 :
            continue

    # 소수 검사
    # 2부터 해당 숫자의 제곱근까지 나눠보며 나누어 떨어지는 수가 있는지 확인
        prinum = True
        for i in range(2, int(int(w) ** 0.5) + 1) :
            if int(w) % i == 0 :
                prinum = False
                break
    # 나누어 떨어지는 수가 없다면 소수로 판단하고 cnt += 1
        if prinum :
            cnt += 1
    return cnt