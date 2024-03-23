N, M = map(int, input().split())
arr = list(map(int,input().split()))

cnt = 0
sm = 0
end = 0

for start in range(N) :
    while end < N and sm < M :
        sm += arr[end]
        end += 1
    if sm == M :
        cnt += 1
    sm -= arr[start]

print(cnt)