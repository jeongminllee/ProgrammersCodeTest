from collections import deque

T = int(input())
for _ in range(T) :
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    left = 0
    tmp = res = 0
    q = deque()
    for right in range(N) :
        while left < N + M - 1 and len(q) < M :
            q.append(arr[left % N])
            tmp += arr[left % N]
            left += 1
        if tmp < K :
            res += 1
        q.popleft()
        tmp -= arr[right]
        right += 1
        if N == M :
            break
    print(res)