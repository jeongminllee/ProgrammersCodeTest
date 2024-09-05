aeiou = ('a','e','i','o','u')
while True :
    S = input()
    if S == 'end' :
        break

    # x : 1번 조건, y : 2번 조건, z : 3번 조건
    x = y = z = 0

    # 1. 모음이 하나 이상 등장하는지
    for i in aeiou :
        if i in S :
            x += 1

    if x < 1 :
        print(f'<{S}> is not acceptable.')
        continue

    # 2. 연속해서 모음 또는 자음이 3개 등장하는지
    for i in range(len(S) - 2) :
        if (S[i] in aeiou and S[i+1] in aeiou and S[i+2] in aeiou) or \
            (not(S[i] in aeiou) and not(S[i+1] in aeiou) and not(S[i+2] in aeiou)):
            y = 1

    if y == 1 :
        print(f'<{S}> is not acceptable.')
        continue

    # 3. 같은 글자가 연속해서 2번 등장하는지, ee oo 는 제외
    for i in range(len(S) - 1) :
        if S[i] == S[i + 1] :
            if S[i] == 'e' or S[i] == 'o' :
                continue
            else :
                z = 1

    if z == 1 :
        print(f'<{S}> is not acceptable.')
        continue
    
    # 3가지 제한사항을 다 통과하였다면
    print(f'<{S}> is acceptable.')