import sys
from collections import defaultdict
sys.setrecursionlimit(300_000)

def solution(a, edges):
    # 모든 가중치의 합이 0이 아니면 불가능
    if sum(a) != 0 :
        return -1

    # 이미 모든 가중치가 0이면 0 반환
    if all(weight == 0 for weight in a) :
        return 0

    # 트리 구성
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent) :
        nonlocal answer
        total = a[node] # 현재 노드의 가중치

        # 자식 노드들의 가중치 합산
        for child in graph[node] :
            if child != parent :    # 부모 노드가 아닌 경우에만
                child_weight = dfs(child, node)
                total += child_weight
                # 자식 노드에서 현재 노드로 가중치를 이동시키는 연산 횟수
                answer += abs(child_weight)

        return total

    answer = 0
    dfs(0, -1)  # 루트 노드를 0번 노드로 가정

    return answer if answer <= 10**17 else -1