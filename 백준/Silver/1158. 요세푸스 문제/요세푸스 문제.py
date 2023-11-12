from collections import deque

N, K = map(int, input().split())

lst = deque(i for i in range(1, N + 1))

ans = []
for i in range(1, N + 1) :
    while len(lst) != 1 :
        lst.rotate(-(K - 1))
        ans.append(lst.popleft())
ans.append(lst.popleft())
ans = list(map(str,ans))
print("<" + ", ".join(ans) + ">")