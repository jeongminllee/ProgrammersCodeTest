def solution(score):
    answer = []
    num = [sum(sc) for sc in score]
    sort_arr = sorted(num, reverse = True)
    
    for i in num :
        answer.append(sort_arr.index(i) + 1)
    return answer