def solution(enroll, referral, seller, amount):
    money = [0 for _ in range(len(enroll))]
    dct = {}
    # [1] 이름을 key, 인덱스를 value로 하는 딕셔너리를 만든다.
    for i, e in enumerate(enroll) :
        dct[e] = i
    # 	{'john': 0, 'mary': 1, 'edward': 2, 'sam': 3, 'emily': 4, 'jaimie': 5, 'tod': 6, 'young': 7}
    
    # [2] seller와 amount를 돌면서 이름의 인덱스를 구하고 money에서 그 인덱스에 해당하는 위치(추천인)에 돈을 더한다.
    for s, a in zip(seller, amount) :
        m = a * 100
        # [3] 계속해서 돈을 1/10씩 줄이면서 돈이 0과 같아지거나 그 다음 추천인이 "-" 이면 while 문을 멈춘다.
        while s != "-" and m > 0 :
            idx = dct[s]
            money[idx] += m - m // 10
            m //= 10
            s = referral[idx]
    return money