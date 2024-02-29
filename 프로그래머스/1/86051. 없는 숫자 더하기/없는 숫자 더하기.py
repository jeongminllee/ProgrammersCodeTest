def solution(numbers):
    total = [i for i in range(1, 10)]
    answer = sum(total) - sum(numbers)
    return answer