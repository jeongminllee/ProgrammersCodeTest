def solution(arr, k):
    answer = []
    for i in arr :
        if k % 2 == 0 :
            i += k
            answer.append(i)
        else :
            i *= k
            answer.append(i)
    return answer