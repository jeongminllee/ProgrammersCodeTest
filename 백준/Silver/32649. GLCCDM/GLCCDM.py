A, B, K = map(int, input().split())
div = []
if B % A > 0 :
    print(-1)
    quit()

for i in range(1, int((B//A) ** 0.5) + 1) :
    if B // A % i < 1 :
        div += [B // A // i] + [i] * (i**2 != B//A)

if K > len(div) :
    print(-1)
else :
    print(*[A * div[i] for i in range(K)])