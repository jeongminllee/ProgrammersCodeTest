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


def solution(num_list):
    answer = [0, 0]
    for n in num_list :
        answer[n % 2] += 1
    return answer