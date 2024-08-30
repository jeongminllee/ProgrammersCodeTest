from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge_list = [[i] + list(map(int, input().split())) for i in range(1, M+1)]
if N <= 2 or M <= N-3:
  print(-1)
  exit()

edge_dict = defaultdict(list)
visited = [False]*(N+1)
for i, a, b in edge_list :
  edge_dict[a].append((i, b))
  edge_dict[b].append((i, a))

def dfs(node) :
  visited[node] = True
  node_list = [node]
  edge_list = []
  q = [node]
  while q :
    node = q.pop()
    for idx, nxt in edge_dict[node] :
      if not visited[nxt] :
        visited[nxt] = True
        edge_list.append(idx)
        node_list.append(nxt)
        q.append(nxt)

  return edge_list, node_list, node

edges, nodes, last_nodes = list(), list(), list()
for i in range(1, N+1) :
  if not visited[i] :
    _edges, _nodes, _last_node = dfs(i)
    edges.append(_edges)
    nodes.append(_nodes)
    last_nodes.append(_last_node)

if len(nodes) > 2 :
  print(-1)
  exit()
if len(nodes) == 2 :
  if len(nodes[0]) == len(nodes[1]) :
    print(-1)
    exit()
  print(len(nodes[0]), len(nodes[1]))
  for i in range(2) :
    print(*nodes[i])
    print(*edges[i])
  exit()

edges, nodes, last_node = edges[0], nodes[0], last_nodes[0]
cur_edges = list()
for idx in edges :
  _, a, b = edge_list[idx-1]
  if a == last_node or b == last_node:
    continue
  cur_edges.append(idx)

print(len(nodes)-1, 1)
print(*[n for n in nodes if n != last_node])
print(*cur_edges)
print(last_node)
print()

'''
N <= 2 라면, 다른 크기의 트리 두 개로 나눌 수 없다. N = 1 이면 애초에 트리가 1개이며, N = 2이면 크기가 1인 두 트리로 나눌 수 밖에 없다.
N을 다른 크기의 N1, N2개 정점의 트리로 나누다면, 그 트리의 정점의 개수 N1 - 1, N2 - 1이다. 따라서 M은 ((N1 - 1) + (N2 - 1)) = N - 2
보다 커야 하며, 이보다 정점의 개수가 작다면 트리를 2개로 나눌 수 없다.

다음은 트리를 구성하는 방법이다. DFS/BFS를 사용하면 여러 역할을 동시에 수행할 수 있다.
노드가 속하는 그래프의 모든 노드를 구할 수 있다. 
또한 visited 배열을 사용하는 특성상 스패닝 트리(Spanning Tree)를 구할 수 있다. 모든 탐색에 사용되는 edge를 기록하기만 하면 된다.
마지막으로 탐색한 노드는 무조건 트리의 리프 노드가 된다.

모든 방문하지 않은 점에 대해 DFS / BFS를 사용하면, 현재 주어진 점들과 간선으로 이루어진 모든 그래프와 그 그래프의 스패닝 트리를 구할 수 있다.
여기서 또 조건 분기가 발생한다.

그래프 개수가 2개 초과일 경우 : 이 경우는 서로 다른 크기의 트리 2개가 분할하는 것이 불가능 하므로 return -1
그래프 개수가 2개일 경우 : 이 경우는 그래프에 속하는 노드 개수를 비교한다. 만약 노드 개수가 동일하다면 서로 다른 크기의 트리가 아니므로 return -1
                        그렇지 않다면 각 스패닝 트리의 노드 번호와 간선 번호를 전부 출력한다.
그래프 개수가 1개일 경우 : 단일 스패닝 트리에서 가장 간단히 2개의 트리로 나눌 수 있는 경우는, 리프 노드 하나를 떼어 새로운 트리를 구성하는 것이다. 
                    그리고 우리는 앞서 리프 노드가 보장되는 노드 번호를 구할 수 있다. 그 리프 노드와 그 노드가 포함되는 간선을 찾아 제거한다면, 
                    우리는 주어진 점들과 간선들로 트리를 구성할 수 있다.
'''