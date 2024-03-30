def dfs(answer, v, cards) :
    for card in cards :
        if not v[card] :
            box = []
            while card not in box :
                box.append(card)
                card = cards[card - 1]
                v[card] = 1
            answer.append(len(box))
            
def solution(cards):
    result = []
    v = [0] * (len(cards) + 1)
    dfs(result, v, cards)
    
    if result[0] == len(cards) :
        return 0
    else :
        result.sort()
    
    return result[-1] * result[-2]