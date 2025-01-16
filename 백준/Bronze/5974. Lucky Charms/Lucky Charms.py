# length, num of charm, nail
L, C, N = map(int, input().split())
ans = []

for _ in range(C) :
    # charm length, position
    S, P = map(int, input().split())

    ans.append(abs(P-N) + S)

for n in ans :
    print(n)