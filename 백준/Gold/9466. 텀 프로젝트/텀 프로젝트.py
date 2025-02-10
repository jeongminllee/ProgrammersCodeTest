import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10 ** 5)

def main() :
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    visited = [0] * (n + 1)
    finished = [0] * (n + 1)
    cnt = 0

    def dfs(v) :
        nonlocal cnt
        visited[v] = 1
        nxt_v = arr[v]
        # 아직 방문하지 않은 학생이면 DFS 재귀 호출
        if not visited[nxt_v] :
            dfs(nxt_v)

        # 이미 방문한 학생인데, 아직 DFS 처리가 끝나지 않았다면 사이클(팀)을 발견
        elif not finished[nxt_v] :
            tmp = nxt_v
            # 사이클에 포함되는 학생들을 센다
            while tmp != v :
                cnt += 1
                tmp = arr[tmp]
            cnt += 1    # 현재 v도 사이클에 포함
        finished[v] = 1 # DFS 처리 완료

    for i in range(1, n + 1):
        if not visited[i] :
            dfs(i)

    print(n - cnt)

T = int(input())
for _ in range(T) :
    main()