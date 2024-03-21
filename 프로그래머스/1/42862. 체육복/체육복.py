def solution(n, lost, reserve):
    answer = n
    lost = set(lost)
    reserve = set(reserve)
    
    # 여분이 있는데 도난 당한 경우
    lost_and_reserve = lost & reserve
    lost -= lost_and_reserve
    reserve -= lost_and_reserve
    
    # 잃어버린 학생한테 빌려줌.
    for i in reserve :
        if i - 1 in lost : 
            lost.remove(i - 1) 
        elif i + 1 in lost :
            lost.remove(i + 1)
            
    # 그럼에도 없는 학생들 수업에서 제외
    answer -= len(lost)
    return answer