from collections import deque

def bfs(start, end) :
    q = deque()
    q.append(start)

    while q :
        curr = q.popleft()
        for nxt in edges[curr] :
            in_degree[nxt[0]] -= 1
            # 비용이 갱신될 때
            if time[nxt[0]] < time[curr] + nxt[1] :
                time[nxt[0]] = time[curr] + nxt[1]
                # 달려야 하는 도로의 수 갱신
                cnt[nxt[0]] = [curr]
            elif time[nxt[0]] == time[curr] + nxt[1] :
                cnt[nxt[0]].append(curr)

            # 선행 도로를 모두 지났을 때
            if in_degree[nxt[0]] == 0 :
                q.append(nxt[0])

    q = deque()
    q.append(end)

    while q :
        curr = q.popleft()
        for x in cnt[curr] :
            if (curr, x) not in v_set :
                v_set.add((curr, x))
                q.append(x)


n = int(input())
m = int(input())

in_degree = [0] * (n+1)
edges = [[] for _ in range(n+1)]
for _ in range(m) :
    departure, destination, weight = map(int, input().split())
    edges[departure].append((destination, weight))
    in_degree[destination] += 1

time = [0] * (n+1)
v_set = set()
cnt = [[] for _ in range(n+1)]

start, end = map(int, input().split())

bfs(start, end)

print(time[end])
print(len(v_set))