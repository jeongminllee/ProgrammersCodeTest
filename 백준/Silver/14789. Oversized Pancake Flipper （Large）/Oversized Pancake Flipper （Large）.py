def main() :
    S, K = input().split()
    S = list(S)
    K = int(K)
    cnt = 0

    for i in range(len(S) - K + 1) :
        if S[i] == '-' :        # 뒤집기가 필요한 경우
            for j in range(K) :
                S[i + j] = '+' if S[i + j] == '-' else '-'
            cnt += 1

    # 모든 펜케이크가 '+' 인지 확인
    if '-' in S :
        return 'IMPOSSIBLE'
    return str(cnt)

T = int(input())
for t in range(1, T+1) :
    print(f"Case #{t}: {main()}")