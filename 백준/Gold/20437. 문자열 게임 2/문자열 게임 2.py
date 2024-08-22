from collections import defaultdict

T = int(input())
for _ in range(T) :
    W = input()
    K = int(input())
    n = len(W)

    dct = defaultdict(list) # key값이 없으면 빈 리스트라도 넣게하기 위해

    for i in range(n) :
        if W.count(W[i]) >= K : # 개수가 K개 이상인 문자들에 대해서만
            dct[W[i]].append(i) # 문자 별로 좌표를 저장 (ex [a]:[0, 4, 9])

    if not dct :    # K 개 이상인 문자가 없으면 아예 불가능
        print(-1)

    else :
        mn = 10000  # 최소값
        mx = 1      # 최대값

        for alpha in dct :  # dct에 있는 특정 문자 alpha에 대해
            for i in range(len(dct[alpha]) - K + 1) :   # 특정 문자의 개수 - 필요 개수 + 1만큼 가능
                length = dct[alpha][i+K-1] - dct[alpha][i] + 1  # 특정 문자의 좌표들 간의 간격 + 1 이 문자열 길이가 된다.
                
                # 최소값, 최대값 갱신
                mn = min(mn, length)
                mx = max(mx, length)

        print(mn, mx)