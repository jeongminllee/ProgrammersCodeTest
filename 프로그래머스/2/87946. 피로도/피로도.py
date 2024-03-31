# def solution(k, dungeons):
#     visited = [0] * len(dungeons)   # 던전 방문 여부를 체크할 리스트
#     answer = [0]    # 탐험할 수 있는 최대 던전 수를 저장할 리스트

#     def dfs(k, cnt) :
#         for i in range(len(dungeons)) :
#             # 아직 방문하지 않았고, 현재 피로도로 탐험 가능한 던전인 경우
#             if not visited[i] and k >= dungeons[i][0] :
#                 visited[i] = 1  # 던전 방문 처리
#                 dfs(k - dungeons[i][1], cnt + 1)    # 탐험 후 피로도 감소
#                 visited[i] = 0  # 던전 방문 처리 해제
#         answer[0] = max(answer[0], cnt) # 최대 던전 탐험 횟수 갱신
        
#     dfs(k, 0)   # 재귀 함수 시작
#     return answer[0]

def solution(k, dungeons):
    answer = -1
    v = [0] * len(dungeons)

    def dfs(k, cnt) :
        nonlocal answer
        for i in range(len(dungeons)) :
            if k >= dungeons[i][0] and not v[i] :
                v[i] = 1
                dfs(k - dungeons[i][1], cnt + 1)
                v[i] = 0
        answer = max(cnt, answer)

    dfs(k, 0)
    return answer