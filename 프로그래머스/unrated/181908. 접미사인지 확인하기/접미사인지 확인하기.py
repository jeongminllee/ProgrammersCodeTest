def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)) :
        ans = [my_string[i:]]
        for a in ans :
            if is_suffix == a :
                answer = 1
    return answer