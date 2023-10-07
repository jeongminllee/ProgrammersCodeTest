def solution(babbling):
    answer = 0
    anna = ["aya", "ye", "woo", "ma"]
    
    for bb in babbling :
        for a in anna :
            bb = bb.replace(a, ' ')
        bb = bb.replace(' ', '')
        if len(bb) == 0 :
            answer += 1
    return answer