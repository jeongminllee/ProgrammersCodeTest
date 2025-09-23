def solution(s):
    answer = [0, 0] # 이진 변환 횟수, 제거된 모든 0의 개수
    
    cnt_1 = cnt_0 = 0
    
    while s != '1' :
        num = ''
        cnt_1 = s.count('1')
        cnt_0 = s.count('0')
        
        answer[1] += cnt_0  # 제거된 모든 0의 개수
        
        while cnt_1 != 0 :
            num += str(cnt_1 % 2)
            cnt_1 //= 2
        
        answer[0] += 1
        s = num[::-1]
        
    
    return answer