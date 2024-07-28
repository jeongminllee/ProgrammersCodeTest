N, K, A, B = map(int, input().split())
lst = [K] * N
cnt = 0

while 0 not in lst :
    for i in range(A) :
        lst[i] += B

    for i in range(N) :
        lst[i] -= 1

    lst.sort()
    cnt += 1

print(cnt)