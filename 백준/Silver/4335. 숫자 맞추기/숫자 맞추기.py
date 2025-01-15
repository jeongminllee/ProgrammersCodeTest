while True:
    high = []  # 높다고 말한 숫자들을 저장하는 리스트
    low = []   # 낮다고 말한 숫자들을 저장하는 리스트
    right = 0  # 정답인 숫자
    
    while True:
        num = int(input())
        if num == 0:  # 0이 입력되면 프로그램 종료
            exit()
            
        response = input()
        
        if response[4] == 'h':    # 현재 숫자가 high인 경우
            high.append(num)
        elif response[4] == 'l':   # 현재 숫자가 low인 경우
            low.append(num)
        else:                      # 현재 숫자가 right인 경우
            right = num
            break
    
    is_true = True
    
    # high에 저장된 모든 값들이 정답보다 큰지 확인
    for h in high:
        if right >= h:
            is_true = False
            break
    
    # low에 저장된 모든 값들이 정답보다 작은지 확인
    if is_true:
        for l in low:
            if right <= l:
                is_true = False
                break
    
    # 결과 출력
    if is_true:
        print("Stan may be honest")
    else:
        print("Stan is dishonest")