def solution(players, callings):
    # 선수 이름 : 순위
    rank = {player : i for i, player in enumerate(players)}
    
    # 호출을 처리하며 순위 변경
    for call in callings :
        # 호출된 선수의 현재 순위
        curr = rank[call]
        
        # 앞선 선수와의 자리 바꾸기
        if curr > 0 :
            # 앞선 선수의 이름
            prev = players[curr - 1]
        
            # 순위 업데이트
            rank[call] -= 1
            rank[prev] += 1
            
            # players 배열에서 두 선수의 위치를 교환
            players[curr - 1], players[curr] = call, prev

    return players