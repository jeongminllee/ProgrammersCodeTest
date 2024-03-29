def dfs(computers, visited, node) :
    visited[node] = 1
    for idx, connected in enumerate(computers[node]) :
        if connected and not visited[idx] :
            dfs(computers, visited, idx)

def solution(n, computers) :
    answer = 0
    visited = [0] * n
    for i in range(n) :
        if not visited[i] :
            dfs(computers, visited, i)
            answer += 1
    return answer
#
# def solution(n, computers):
#     answer = 0
#     visited = [False for _ in range(n)]
#     for com in range(n) :
#         if visited[com] == False :
#             DFS(n, computers, com, visited)
#             # BFS(n, computers, com, visited)
#             answer += 1
#     return answer
#
# def DFS(n, computers, com, visited) :
#     visited[com] = True
#     for connect in range(n) :
#         if connect != com and computers[com][connect] == 1 : # 연결된 컴퓨터
#             if visited[connect] == False :
#                 DFS(n, computers, connect, visited)
#
# def BFS(n, computers, com, visited) :
#     visited[com] = True
#     queue = []
#     queue.append(com)
#     while len(queue) != 0 :
#         com = queue.pop(0)
#         visited[com] = True
#         for connect in range(n) :
#             if connect != com and computers[com][connect] == 1:
#                 if visited[connect] == False :
#                     queue.append(connect)