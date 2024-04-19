def solution(cards):
    answer = []
    v = [0] * (len(cards) + 1)
    
    for card in cards :
        if not v[card] :
            box = []
            while card not in box :
                box.append(card)
                card = cards[card-1]
                v[card] = 1
            answer.append(len(box))
            
    if len(answer) < 2:
        return 0
    else :
        answer.sort()
        
    return answer[-1] * answer[-2]