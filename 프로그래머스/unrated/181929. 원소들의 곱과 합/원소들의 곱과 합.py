def solution(num_list):
    answer = 0
    product = 1
    for num in num_list :
        product *= num
    
    sum2 = sum(num_list) ** 2
    
    if sum2 > product :
        answer = 1
    else :
        answer = 0
    return answer