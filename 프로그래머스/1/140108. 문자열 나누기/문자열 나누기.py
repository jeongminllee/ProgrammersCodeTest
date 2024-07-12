def solution(s):
    answer = 0
    
    while s :
        x = s[0]
        x_cnt = 0
        other_cnt = 0
        
        for i, char in enumerate(s) :
            if char == x :
                x_cnt += 1
            else :
                other_cnt += 1
                
            if x_cnt == other_cnt :
                answer += 1
                s = s[i+1:]
                break
                
        else :  # x_cnt와 other_cnt가 같아지지 않은 채로 문자열 끝에 도달한 경우
            answer += 1
            break
            
    return answer