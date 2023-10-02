def solution(n):
    answer = 0
    numlist = list(str(n))
    for num in numlist :
        answer += int(num)
    return answer