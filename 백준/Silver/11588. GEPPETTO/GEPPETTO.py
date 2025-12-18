N, M = map(int, input().split())
forbidden = [0] * M
for m in range(M) :
    a, b = map(int, input().split())
    forbidden[m] = (1<<(a-1) | 1<<(b-1))

cnt = 2 ** N
for n in range(1<<N) :
    for banned in forbidden :
        if n & banned == banned :
            cnt -= 1
            break
print(cnt)