def solution(n, results):
    # 승패 관계를 저장할 2차원 리스트 초기화
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    # 주어진 경기 결과로 승패 관계 설정
    for w, l in results :
        graph[w][l] = 1
        graph[l][w] = -1
        
    # Floyd-Warshall 알고리즘
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(n+1) :
                if graph[i][k] == 1 and graph[k][j] == 1 :
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1 :
                    graph[i][j] = -1
                    
    # 각 선수의 순위를 알 수 있는지 확인    
    answer = 0
    for i in range(1, n+1) :
        if sum(1 for j in range(1, n+1) if graph[i][j] != 0 or graph[j][i] != 0) == n-1 :
            answer += 1
    return answer