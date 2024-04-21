from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(p) :
    start = []
    for i in range(5) : # 시작점이 되는 P좌표 구하기
        for j in range(5) :
            if p[i][j] == 'P' :
                start.append((i, j))

    for s in start :
        q = deque()
        q.append(s)
        v = [[0] * 5 for _ in range(5)] # 방문 처리 리스트
        d = [[0] * 5 for _ in range(5)] # 경로 길이 리스트
        v[s[0]][s[1]] = 1

        while q :
            x, y = q.popleft()

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and v[nx][ny] == 0 :
                    if p[nx][ny] == 'O' :
                        q.append((nx, ny))
                        v[nx][ny] = 1
                        d[nx][ny] = d[x][y] + 1

                    if p[nx][ny] == "P" and d[x][y] <= 1 :
                        return 0
    return 1

def solution(places):
    answer = []

    for i in places :
        answer.append(bfs(i))

    return answer

# def solution(places):
#     answer = []
    
#     for p in places :
#         # 거리두기가 지켜지지 않음을 확인하면 바로 반복을 멈추기 위한 flag
#         flag = False
#         nowArr = []
        
#         # 이번 place를 nowArr에 담아줌
#         for n in p :
#             nowArr.append(list(n))
            
#         # 이중 for문을 이용해 하나씩 확인함.
#         for i in range(5) :
#             if flag :
#                 break
                
#             for j in range(5) :
#                 if flag :
#                     break
                
#                 # 사람을 찾아내면 판단을 시작
#                 if nowArr[i][j] == "P" :
                    
#                     if i+1 < 5 :
#                         # 만약 바로 아랫부분에 사람이 존재하면 break
#                         if nowArr[i+1][j] == "P" :
#                             flag = True
#                             break
#                         # 만약 아랫부분이 빈 테이블이고 그 다음에 바로 사람이 있다면 한 칸 떨어져 있더라도 맨해튼 거리는 2이므로 break
#                         if nowArr[i+1][j] == "O" :
#                             if i+2 < 5 :
#                                 if nowArr[i+2][j] == "P" :
#                                     flag=True
#                                     break
                                    
#                     # 바로 오른쪽 부분에 사람이 존재하면 break
#                     if j+1 < 5 :
#                         if nowArr[i][j+1] == "P" :
#                             flag = True
#                             break
#                         # 만약 오른쪽 부분이 빈 테이블이고 그 다음에 바로 사람이 있다면 한 칸 떨어져 있더라도 맨해튼 거리는 2이므로 break
#                         if nowArr[i][j+1] == "O" :
#                             if j+2 < 5 :
#                                 if nowArr[i][j+2] == "P" :
#                                     flag = True
#                                     break
#                     # 우측 아래 부분
#                     if i+1 < 5 and j+1 < 5 :
#                         # 만약 우측 아래가 사람이고, 오른쪽 또는 아랫부분 중 하나라도 빈 테이블이면 break
#                         if nowArr[i+1][j+1] == "P" and (nowArr[i+1][j] == "O" or nowArr[i][j+1]=="O") :
#                             flag = True
#                             break
                    
#                     # 좌측 아래
#                     if i+1 < 5 and j - 1 >= 0 :
#                         # 만약 좌측 아래가 사람이고, 왼쪽 또는 아랫부분 중 하나라도 빈 테이블이면 break
#                         if nowArr[i+1][j-1]=="P" and (nowArr[i+1][j] == "O" or nowArr[i][j-1] == "O") :
#                             flag = True
#                             break
        
#         # 위의 for문 동안 flag가 True로 변경되었다면 거리두기가 지켜지지 않은 것이므로 0을 answer에 추가
#         if flag :
#             answer.append(0)
#         # flag가 False로 끝났다면 거리두기가 지켜졌으므로 1을 추가
#         else :
#             answer.append(1)
            
#     return answer