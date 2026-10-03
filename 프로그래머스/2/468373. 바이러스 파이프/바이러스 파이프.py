from collections import deque

GLOBAL_ANSWER = 1

def bfs(infect_set, graph, type) :
    
    q = deque(infect_set)
    nxt_infect = infect_set.copy()

    while q :
        curr_node = q.popleft()
        for nxt_node, nxt_type in graph[curr_node] :
            if nxt_type == type and nxt_node not in nxt_infect :
                nxt_infect.add(nxt_node)
                q.append(nxt_node)

    return nxt_infect

def dfs(infect_set, graph, k, cnt, last_type) :
    global GLOBAL_ANSWER
    GLOBAL_ANSWER = max(GLOBAL_ANSWER, len(infect_set))

    if cnt == k :
        return

    curr_infect_set = infect_set.copy()

    for nxt_type in range(1, 4) :
        if nxt_type == last_type :
            continue
        new_infect_set = bfs(curr_infect_set, graph, nxt_type)

        dfs(new_infect_set, graph, k, cnt+1, nxt_type)


def solution(n, infection, edges, k):
    global GLOBAL_ANSWER
    infect_set = set([infection]) # 감염된 배양체 

    graph = [[] for _ in range(n+1)]    # 1부터 시작이네
    for x, y, type in edges :
        graph[x].append([y, type])
        graph[y].append([x, type])

    dfs(infect_set, graph, k, 0, -1)
    return GLOBAL_ANSWER