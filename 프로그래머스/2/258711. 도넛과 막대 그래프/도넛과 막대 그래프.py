from collections import defaultdict

def solution(edges):
    # 각 노드의 진입 차수와 진출 차수를 저장할 딕셔너리 초기화
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    # 모든 고유한 노드를 저장할 집합
    nodes = set()

    # 간선 정보를 순회하며 각 노드의 진입/진출 차수 계산 및 노드 집합 업데이트
    for a, b in edges:
        out_degree[a] += 1
        in_degree[b] += 1
        nodes.add(a)
        nodes.add(b)

    # 생성된 정점과 각 그래프 유형의 수를 저장할 변수 초기화
    created_node = None
    donut = bar = eight = 0

    # 모든 노드를 순회하며 각 그래프 유형 분류
    for node in nodes:
        if out_degree[node] >= 2 and in_degree[node] == 0:
            # 진출 차수 >= 2이고 진입 차수 = 0인 노드는 생성된 정점
            created_node = node
        elif out_degree[node] == 0:
            # 진출 차수 = 0인 노드는 막대 모양 그래프의 끝점
            bar += 1
        elif out_degree[node] == 2:
            # 진출 차수 = 2인 노드는 8자 모양 그래프의 중심점
            eight += 1

    # 도넛 모양 그래프의 수 계산
    # 생성된 정점의 진출 차수에서 막대와 8자 모양 그래프의 수를 뺀 값
    donut = out_degree[created_node] - bar - eight

    # 문제에서 요구하는 순서대로 결과 반환
    # [생성된 정점의 번호, 도넛 모양 그래프 수, 막대 모양 그래프 수, 8자 모양 그래프 수]
    return [created_node, donut, bar, eight]