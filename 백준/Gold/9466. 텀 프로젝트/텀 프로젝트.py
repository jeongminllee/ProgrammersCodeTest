def main() :
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    visited = [0] * (n + 1)
    finished = [0] * (n + 1)
    cnt = 0

    for i in range(1, n + 1) :
        if visited[i] :
            continue

        # 각 DFS마다 현재 경로를 기록
        stack = []
        cur = i

        while True :
            visited[cur] = 1
            stack.append(cur)
            nxt = arr[cur]

            # 아직 방문하지 않았다면 계속 진행
            if not visited[nxt] :
                cur = nxt
                continue

            # 방문한 적은 있지만, DFS 처리가 끝나지 않은 경우 => 현재 경로에 있으므로 사이클 발견
            if not finished[nxt] :
                # 스택에서 nxt가 처음 등장한 인덱스를 찾고, 그 이후의 노드들이 사이클에 속함
                idx = stack.index(nxt)
                cnt += len(stack) - idx
            # 더 이상 진행할 수 없으므로 탈출
            break

        # 현재 DFS 경로에 있는 모든 노드에 대해 finished 처리
        for node in stack :
            finished[node] = 1

    print(n - cnt)

T = int(input())
for _ in range(T) :
    main()