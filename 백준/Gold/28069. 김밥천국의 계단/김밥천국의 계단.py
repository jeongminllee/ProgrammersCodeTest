N, K = map(int, input().split())
for _ in range(K) :
    # 계산 steps = steps + 1, (steps + steps//2 = steps * 3 // 2)
    # 결국 N == steps 가 되어야 하므로 N = steps + 1, (steps + steps//2 = steps * 3 // 2)
    # steps = N - 1, N * 2 // 3
    # 나누기 3을 하게 되면 오차가 발생하기 때문에 보정을 해주어야 함.
    # i = 2t 면, i + i/2 = 2t + t = 3t = N 이기 때문에 i = 2n / 3
    # i = 2t + 1 이면, i + i/2 = 2t+1 + t = 3t+1 = N 이기 때문에 i = 2n//3 + 1
    if N % 3 <= 1 :
        N = min(N - 1, 2 * N // 3 + N % 3)
    else :
        N -= 1

    if N <= 0 :
        break

if N <= 0:
    print("minigimbob")
else :
    print("water")