from collections import deque

INF = 10 ** 9

def main() :
    N = int(input())
    lst = list(map(int, input().split()))
    
    if N == 1 :
        print(0)
        return
    
    if lst[0] == 0 :
        print(-1)
        return

    q = deque()
    q.append((lst[0], 0, 0))   # start, idx, cnt
    v = [INF] * N             # 중복방지
    v[0] = 0

    while q :
        curr, idx, cnt = q.popleft()
        if idx == N-1 :
            print(cnt)
            return

        for val in range(1, curr+1) :
            nxt = idx + val
            if nxt <= N-1 and v[nxt] > cnt + 1 :
                q.append((lst[nxt], nxt, cnt + 1))
                v[nxt] = cnt + 1

    if v[N-1] == INF :
        print(-1)
        return

if __name__ == "__main__" :
    main()