def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse = True)
    for i in range(n) :
        if citations[i] >= i + 1 :
            answer += 1
    return answer