def solution(numbers):
    answer = 0
    ans = []
    for i in range(len(numbers)):
        for j in range(len(numbers)) :
            if i != j :
                ans.append(numbers[i] * numbers[j])
                answer = max(ans)
    return answer

# def solution(numbers):
#     numbers.sort()
#     return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
