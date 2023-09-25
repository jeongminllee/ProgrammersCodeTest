def solution(numbers):
    answer = 0
    number = 0
    for i, val in enumerate(numbers) :
        number += val
        answer = number / len(numbers)
    return answer