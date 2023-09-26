def solution(num_list):
    answer = []
    odds = []
    evens = []
    for i in range(len(num_list)) :
        if num_list[i] % 2 == 0 :
            evens.append(num_list[i])
        else :
            odds.append(num_list[i])
        
    return [len(evens), len(odds)]