import sys
from collections import deque

def bfs(s, e) :
    q = deque()
    v = [0] * (F + 1)

    q.append(s)
    v[s] = 1    # return 할때는 -1로 리턴

    while q :
        c = q.popleft()
        if c == e :
            return v[c] - 1
        # 2방향, 범위 내, 미방문
        for n in (c + U, c - D) :
            if 1 <= n <= F and v[n] == 0 :
                q.append(n)
                v[n] = v[c] + 1

    # 목적지를 찾을 수 없는 경우
    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
ans = bfs(S, G)
print(ans)

