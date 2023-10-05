def solution(numbers):
    answer = 0
    ans = []
    for i in range(len(numbers)):
        for j in range(len(numbers)) :
            if i != j :
                ans.append(numbers[i] * numbers[j])
                answer = max(ans)
    return answer