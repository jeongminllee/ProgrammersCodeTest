"""
k=1 일때는 해결하겠는데 k <= 24 일떄는 모르겠네 

"""

def solution(players, m, k):
    answer = 0
    server = []
    for player in players :
        
        # 각 서버별 제한시간을 설정
        for i in range(len(server)) :
            server[i] -= 1
        
        # 서버 시간이 종료(0)이면 그 서버를 큐에서 제거.
        while server.__contains__(0):
            server.remove(0)
                
        # 현재 열려있는 서버를 체크한다. 
        current_server = len(server)
        available_user = m * current_server
        
        # 서버 추가를 얼마나 해야하는지 체크
        if player > available_user:
            new_server = (player - available_user) // m
            if new_server >= 1 :
                answer += new_server
                for i in range(new_server) :
                    server.append(k)
                    
    return answer