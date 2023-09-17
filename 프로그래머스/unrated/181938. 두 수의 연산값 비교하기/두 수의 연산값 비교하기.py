def solution(a, b):
    answer1 = str(a) + str(b)
    answer2 = 2 * a * b
    return int(answer1) if int(answer1) > int(answer2) else int(answer2) 