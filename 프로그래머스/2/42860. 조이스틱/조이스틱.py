def solution(name):
    answer = 0
    # 초기 이동 횟수 초기값 설정
    min_move = len(name) - 1
    
    for i, char in enumerate(name) :
        # 알파벳 변경 최소 횟수 추가
        answer += min(ord(char) - ord("A"), ord("Z") - ord(char) + 1)
        
        nxt = i + 1
        # 다음 "A" 가 아닌 문자까지 이동
        while nxt < len(name) and name[nxt] == "A" :
            nxt += 1
        
        # 현재 위치에서 다음 "A"가 아닌 문자까지의 최소 거리
        distance = min(i, len(name) - nxt)
        # 최소 이동 횟수 갱신
        min_move = min(min_move, i + len(name) - nxt + distance)
        
    answer += min_move
    return answer