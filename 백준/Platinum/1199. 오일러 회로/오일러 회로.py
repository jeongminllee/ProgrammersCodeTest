def main() :
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    degree = [sum(now) for now in graph]

    for i in degree :
        if i % 2 :
            print(-1)
            exit()

    start = 0
    ptr = [0] * N
    stack = [start]

    while stack :
        node = stack[-1]

        while ptr[node] < N and not graph[node][ptr[node]] :
            ptr[node] += 1

        if ptr[node] == N :
            print(stack.pop() + 1, end=' ')

        else :
            graph[node][ptr[node]] -= 1
            graph[ptr[node]][node] -= 1
            stack.append(ptr[node])
            


if __name__ == '__main__' :
    main()