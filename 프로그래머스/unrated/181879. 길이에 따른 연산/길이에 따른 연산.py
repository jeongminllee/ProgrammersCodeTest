def solution(num_list):
    answer = 1
    for i in num_list :
        if len(num_list) > 10 :
            answer = sum(num_list)
        else :
            answer *= i
            
    return answer