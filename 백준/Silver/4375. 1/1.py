while True :
    try :
        n = int(input())

    except :
        break

    num = 1     # 1로만 이루어진 수
    cnt = 1     # 자릿수

    while True :
        if num % n != 0 :       # n의 배수가 아니라면
            num = num * 10 + 1  # 1로만 이루어진 다음 수로 갱신
            cnt += 1            # 자리수 세어줌

        else :                  # n의 배수라면
            break               # 종료
        
    print(cnt)