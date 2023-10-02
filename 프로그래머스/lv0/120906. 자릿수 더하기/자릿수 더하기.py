def solution(n):
    answer = 0
    numlist = str(n)
    for num in numlist :
        answer += int(num)
    return answer