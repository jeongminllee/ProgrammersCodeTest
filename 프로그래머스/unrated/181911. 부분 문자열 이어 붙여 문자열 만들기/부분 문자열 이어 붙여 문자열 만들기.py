def solution(my_strings, parts):
    answer = ''
    for idx, (s, e) in enumerate(parts) :
        answer += my_strings[idx][s : e + 1]
    return answer