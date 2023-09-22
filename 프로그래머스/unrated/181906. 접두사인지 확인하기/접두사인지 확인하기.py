def solution(my_string, is_prefix):
    answer = 0
    for i in range(len(my_string)) :
        ans = [my_string[:i+1]]
        for a in ans :
            if is_prefix == a :
                answer = 1
    return answer