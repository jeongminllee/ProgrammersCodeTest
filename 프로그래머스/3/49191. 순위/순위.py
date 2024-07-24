# def solution(n, results):
#     # 승패 관계를 저장할 2차원 리스트 초기화
#     graph = [[0] * (n+1) for _ in range(n+1)]
    
#     # 주어진 경기 결과로 승패 관계 설정
#     for w, l in results :
#         graph[w][l] = 1
#         graph[l][w] = -1
        
#     # Floyd-Warshall 알고리즘
#     for k in range(1, n+1) :
#         for i in range(1, n+1) :
#             for j in range(n+1) :
#                 if graph[i][k] == 1 and graph[k][j] == 1 :
#                     graph[i][j] = 1
#                 elif graph[i][k] == -1 and graph[k][j] == -1 :
#                     graph[i][j] = -1
                    
#     # 각 선수의 순위를 알 수 있는지 확인    
#     answer = 0
#     for i in range(1, n+1) :
#         if sum(1 for j in range(1, n+1) if graph[i][j] != 0 or graph[j][i] != 0) == n-1 :
#             answer += 1
#     return answer

from collections import defaultdict

def solution(n, results):
    answer = 0
    # 각 선수의 승리와 패배 기록을 저장할 defaultdict 생성
    # key: 선수 번호, value: 해당 선수가 이긴/진 선수들의 집합
    win, lose = defaultdict(set), defaultdict(set)

    # 주어진 경기 결과를 바탕으로 직접적인 승패 관계 설정
    for winner, loser in results:
        lose[loser].add(winner)  # loser가 winner에게 졌음을 기록
        win[winner].add(loser)   # winner가 loser를 이겼음을 기록

    # 간접적인 승패 관계까지 고려하여 승패 관계 업데이트
    for i in range(1, n+1):
        # i에게 진 선수들은 i가 이긴 모든 선수들도 이김
        for winner in lose[i]:
            win[winner].update(win[i])
        # i에게 이긴 선수들은 i가 진 모든 선수들에게도 짐
        for loser in win[i]:
            lose[loser].update(lose[i])

    # 각 선수에 대해 순위를 확실히 알 수 있는지 확인
    for i in range(1, n + 1):
        # i의 승패가 확실한 경우의 수 = (i가 이긴 선수 수) + (i가 진 선수 수)
        # 이 값이 n-1이면 i의 순위를 확실히 알 수 있음 (자기 자신 제외)
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
            
    return answer