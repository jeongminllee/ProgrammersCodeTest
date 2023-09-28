def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    answer = numbers[-1] * numbers[-2]
    return answer