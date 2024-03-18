def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for i, char in enumerate(name) :
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
        
        nxt = i + 1
        while nxt < len(name) and name[nxt] == "A" :
            nxt += 1
        
        distance = min(i, len(name) - nxt)
        min_move = min(min_move, i + len(name) - nxt + distance)
        
    answer += min_move
    return answer