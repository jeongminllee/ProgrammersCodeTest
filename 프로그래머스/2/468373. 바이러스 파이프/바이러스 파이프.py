"""
트리, 그래프 문제인듯?
edges[i] = [x, y, type]

단계별로 열리는거 + 동시에 일어남
이거는 DFS, BFS 같이 써야되는거 같은데
k는 조합의 갯수니까 1 이 선택되면 1로 갈 수 있는 모든 방향으로 전진한다. 음... 
n = 100, k = 10, type = 3 
1 -> a(2, 3), b(5), c(4) 
    2, 3 -> a(-), b(5, 9), c(4, 8) => 1, 2, 3, 5, 9 or 1, 2, 3, 4, 8 
    5 -> a(2, 3, 6, 7), b(-), c(4) => 1, 2, 3, 5, 6 ,7
    4 -> a(2, 3), b(5), c(-) => 1, 2, 3, 4
    
=> 6
BFS는 괜찮아 보이는데 DFS는 괜찮나 -> 일단 해보자.

"""
from collections import deque
   
def solution(n, infection, edges, k):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for start, end, pipe in edges :
        graph[start].append([end, pipe])
        graph[end].append([start, pipe])
    
    res = {infection}
    max_infected = 1
    def dfs(curr_infected, cnt, last_pipe) :
        nonlocal answer
        answer = max(answer, len(curr_infected))
        if cnt == k :
            return
        
        for nxt_pipe in range(1, 4) :
            if nxt_pipe == last_pipe :
                continue
            
            new_res = bfs(curr_infected, nxt_pipe)
            
            dfs(new_res, cnt + 1, nxt_pipe)
            
    def bfs(curr_infected, pipe) :
        q = deque(curr_infected)
        nxt_infected = curr_infected.copy()
        while q :
            node = q.popleft()
            for nxt_node, nxt_pipe in graph[node] :
                if nxt_pipe == pipe and nxt_node not in nxt_infected :
                    nxt_infected.add(nxt_node)
                    
                    q.append(nxt_node)
        
        return nxt_infected
    
    dfs(res, 0, -1)
    return answer