N, K = map(int, input().split())
arr = list(map(int,input().split()))

sm = sum(arr[:K])
max_sm = sm

for i in range(K, N) :
    sm += arr[i] - arr[i - K]
    max_sm = max(sm, max_sm)

print(max_sm)