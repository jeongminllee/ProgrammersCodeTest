def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]
    
    for word in babbling :
        val = True
        prev = ""
        i = 0
        
        while i < len(word) :
            flag = False
            for speak in lst :
                if word[i : i + len(speak)] == speak and speak != prev :
                    flag = True
                    prev = speak
                    i += len(speak)
                    break
            if not flag :
                val = False
                break
                
        if val :
            answer += 1
            
    return answer