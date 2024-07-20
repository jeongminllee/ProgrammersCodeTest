def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf) :
        if sheep > wolf :
            answer.append(sheep)
        else :
            return

        for p, c in edges :
            if visited[p] and not visited[c] :
                visited[c] = 1
                if info[c] == 0 :
                    dfs(sheep + 1, wolf)
                else :
                    dfs(sheep, wolf + 1)
                visited[c] = 0

    visited[0] = 1
    dfs(1, 0)

    return max(answer)

# from collections import deque

# def solution(info, edges):
#     tree = [[] for _ in range(len(info))]
#     for edge in edges :
#         tree[edge[0]].append(edge[1])

#     sheep = 0

#     q = deque()
#     q.append((0, 1, 0, set()))

#     while q:
#         curr, sheep_cnt, wolf_cnt, visited = q.popleft()
#         sheep = max(sheep, sheep_cnt)
#         visited.update(tree[curr])

#         for next_node in visited :
#             if info[next_node] :
#                 if sheep_cnt != wolf_cnt + 1 :
#                     q.append((next_node, sheep_cnt, wolf_cnt + 1, visited - {next_node}))
#             else :
#                 q.append((next_node, sheep_cnt + 1, wolf_cnt, visited - {next_node}))

#     return sheep