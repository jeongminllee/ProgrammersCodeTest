def solution(s):
    answer = 0
    string = s.split(' ')
    for i, num in enumerate(string) :
        if num == 'Z' :
            string[i] = '-' + string[i - 1]
            if '--' in string[i]:
                string[i] = string[i].replace('--', '')

    for a in string :
        answer += int(a)
    return answer