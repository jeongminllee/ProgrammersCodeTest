from collections import deque

INF = 1<<32

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, arr) :
    R, C = len(arr), len(arr[0])
    q = deque()
    q.append((si, sj))

    distances[0][0] = 0

    while q :
        ci, cj = q.popleft()
        curr = distances[ci][cj]

        for d in range(4) :
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<R and 0<=nj<C :
                cost = 1 if arr[ni][nj] == 1 else 0
                nd = curr + cost
                if distances[ni][nj] > nd :
                    distances[ni][nj] = nd
                    if cost == 0 :
                        q.appendleft((ni, nj))
                    else :
                        q.append((ni, nj))


def main() :
    global distances
    R, C = map(int, input().split())
    arr = [[0 for _ in range(C+2)] for _ in range(R+2)]

    for i in range(1, R+1) :
        arr[i] = [0] + list(map(int, input().split())) + [0]

    distances = [[INF for _ in range(C+2)] for _ in range(R+2)]

    bfs(0, 0, arr)

    broken = -1
    cnt = 0
    for i in range(1, R+1) :
        for j in range(1, C+1) :
            if arr[i][j] == 0 :
                if distances[i][j] > broken :
                    broken = distances[i][j]
                    cnt = 1
                elif distances[i][j] == broken :
                    cnt += 1

    print(broken, cnt)


if __name__ == "__main__" :
    T = int(input())
    for _ in range(T) :
        main()