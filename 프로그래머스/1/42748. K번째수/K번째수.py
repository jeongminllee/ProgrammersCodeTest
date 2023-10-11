def solution(array, commands):
    answer = []
    for i, j, k in commands :
        array_ = array[i-1: j]
        sorted_array = sorted(array_)
        
        answer.append(sorted_array[k-1])
    return answer