import sys
input = sys.stdin.readline
from collections import deque

def main() :
    A, B = map(int, input().split())

    visited = [0] * 10001

    q = deque()
    q.append([A, ''])
    visited[A] = 1

    while q :
        num, command = q.popleft()

        if num == B:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d] :
            visited[d] = 1
            q.append([d, command + 'D'])

        s = (num - 1) % 10000
        if not visited[s] :
            visited[s] = 1
            q.append([s, command + 'S'])

        l = num // 1000 + (num % 1000) * 10
        if not visited[l] :
            visited[l] = 1
            q.append([l, command + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r] :
            visited[r] = 1
            q.append([r, command + 'R'])


T = int(input())
for _ in range(T) :
    main()