def solution(numLog):
    answer = ''
    dic = {1:'w', -1:'s', 10:'d', -10:'a'}
    
    for index, valid in enumerate(numLog) :
        if index != len(numLog) - 1 :
            answer += dic[numLog[index+1] - numLog[index]]
            
    return answer