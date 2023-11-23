from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (N + 1)
distance[X] = 0

q = deque()
q.append(X)
while q :
    now = q.popleft()
    for next_now in graph[now] :
        if distance[next_now] == -1 :
            distance[next_now] = distance[now] + 1
            q.append(next_now)

check = 0
for i in range(1, N + 1) :
    if distance[i] == K :
        print(i)
        check = 1

if check == 0 :
    print(-1)