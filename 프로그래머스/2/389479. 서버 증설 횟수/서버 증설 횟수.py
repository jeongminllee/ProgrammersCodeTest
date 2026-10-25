"""
k=1 일때는 해결하겠는데 k <= 24 일떄는 모르겠네 

"""

def solution(players, m, k):
    answer = 0
    server = []
    for player in players :
        
        for i in range(len(server)) :
            server[i] -= 1
            
        while server.__contains__(0):
            server.remove(0)
                
        current_server = len(server)
        available_user = m * current_server
        
        if player > available_user:
            new_server = (player - available_user) // m
            if new_server >= 1 :
                answer += new_server
                for i in range(new_server) :
                    server.append(k)
                    
    return answer