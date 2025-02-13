# 12395 : Password Problem
def sol_12395():
    A, B = map(int, input().split())        # 이미 입력한 문자, 전체 문자
    already_key = list(map(float, input().split()))

    ans = 1 << 32
    prod = [1.0]

    for i in range(A) :
        prod.append(prod[-1] * already_key[i])

    # 1. 계속 입력하기(k=0), 백스페이스 이용 (k>=1)
    for k in range(A + 1) :
        cnt = k + (B - A + k + 1) + (1 - prod[A-k]) * (B + 1)
        ans = min(ans, cnt)

    cnt = 1 + B + 1
    ans = min(ans, cnt)

    return ans


T = int(input())
for t in range(1,T+1) :
    print(f"Case #{t}: {sol_12395():.6f}")