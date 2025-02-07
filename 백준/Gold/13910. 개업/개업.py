def main() :
    # 주문 받은 짜장면, 웍 개수
    N, M = map(int, input().split())
    # 웍 용량 리스트
    S = list(map(int, input().split()))

    # 한 번의 요리에서 만들 수 있는 후보 요리량을 구함
    # 단, 웍 하나만 사용할 경우와 두 웍을 같이 사용할 경우 모두 고려
    candidates = set()

    # 1. 단일 웍 사용 : 각 웍의 용량이 후보가 됨 (N보다 작거나 같아야 함)
    for s in S :
        if s <= N :
            candidates.add(s)

    # 2. 두 웍 동시에 사용 : 서로 다른 두 웍의 합 (같은 웍이 두 개 있는 경우도 i < j 로 처리됨)
    for i in range(M) :
        for j in range(i+1, M) :
            sum_val = S[i] + S[j]
            if sum_val <= N :
                candidates.add(sum_val)

    # 후보를 리스트로 변환
    candidates = list(candidates)

    # dp[i]는 i그릇을 만드는 데 필요한 최소 요리 횟수를 차감
    # 초기값은 0그릇을 만드는 데 0회 요리 => dp[0] = 0, 나머지는 아직 만들지 못한 상태로 -1로 표기.
    dp = [-1] * (N + 1)
    dp[0] = 0

    # dp 전이 : 0부터 N까지 간으한 그릇 수에 대해 후보 요리량을 더해 나감.
    for i in range(N + 1) :
        if dp[i] == -1 :    # i그릇을 만들 수 없다면 넘어감
            continue
        # 각 후보 요리량 c를 이용해서 i + c그릇을 만드는 경우를 고려
        for c in candidates :
            if i + c <= N :
                # 아직 i+c그릇을 만드는 최소 횟수를 기록하지 않았거나, 더 적은 요리 횟수를 발견한 경우 갱신
                if dp[i + c] == -1 or dp[i + c] > dp[i] + 1 :
                    dp[i + c] = dp[i] + 1

    print(dp[N])

main()