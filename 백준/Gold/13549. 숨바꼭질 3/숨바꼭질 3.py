from collections import deque

def bfs(s, e) :
    # 1. q 생성, v[] 생성
    q = deque()
    v = [-1] * 100001

    # 2. 초기 데이터 삽입, v[] 초기화
    q.append(s)
    v[s] = 0

    while q :
        c = q.popleft()
        if c == e :
            return v[e]
        
        if 0 < c * 2 < 100001 and v[c * 2] == -1 :
            v[c * 2] = v[c]
            q.append(c * 2)

        if 0 <= c - 1 < 100001 and v[c - 1] == -1 :
            v[c - 1] = v[c] + 1
            q.append(c - 1)

        if 0 <= c + 1 < 100001 and v[c + 1] == -1 :
            v[c + 1] = v[c] + 1
            q.append(c + 1)

        
n, k = map(int, input().split())
res = bfs(n, k)
print(res)