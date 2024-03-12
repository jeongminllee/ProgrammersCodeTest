def solution(s):
    answer = [-1] * len(s)
    result = {}
    for i, char in enumerate(s) :
        if char in result :
            answer[i] = i - result[char]
        result[char] = i
    return answer