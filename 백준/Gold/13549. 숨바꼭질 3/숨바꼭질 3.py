from collections import deque

MAX = 10**5 + 1

def bfs(start, end) :
    v[start] = 0
    q = deque()
    q.append(start)

    while q :
        curr = q.popleft()
        if curr == end :
            return v[curr]

        if 0 < curr * 2 < MAX and v[curr*2] == -1 :
            v[curr * 2] = v[curr]
            q.append(curr * 2)

        if 0 <= curr - 1 < MAX and v[curr - 1] == -1 :
            v[curr - 1] = v[curr] + 1
            q.append(curr - 1)

        if 0 <= curr + 1 < MAX and v[curr + 1] == -1 :
            v[curr + 1] = v[curr] + 1
            q.append(curr + 1)

N, K = map(int, input().split())
v = [-1] * MAX
print(bfs(N, K))