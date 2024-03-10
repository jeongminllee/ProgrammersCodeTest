from collections import deque

def bfs(s, e) :
    q = deque()
    v = [0] * 200001

    q.append(s)
    v[s] = 1

    while q :
        c = q.popleft()
        if c == e :
            return v[e] - 1

        for n in (c - 1, c + 1, c * 2) :
            if 0 <= n <= 200000 and v[n] == 0 :
                q.append(n)
                v[n] = v[c] + 1

    return -1

n, k = map(int, input().split())
print(bfs(n, k))