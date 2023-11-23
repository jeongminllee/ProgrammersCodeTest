from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)
v = [-1 for _ in range(100001)]
v[n] = 0

while q :
    s = q.popleft()
    if s == k :
        print(v[s])
        break
    if 0 <= s - 1 < 100001 and v[s - 1] == -1 :
        v[s - 1] = v[s] + 1
        q.append(s - 1)
    if 0 < s * 2 < 100001 and v[s * 2] == -1 :
        v[s * 2] = v[s]
        q.append(s * 2)
    if 0 <= s + 1 < 100001 and v[s + 1] == -1 :
        v[s + 1] = v[s] + 1
        q.append(s + 1)
        