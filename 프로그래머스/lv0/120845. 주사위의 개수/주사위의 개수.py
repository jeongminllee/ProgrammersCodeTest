def solution(box, n):
    x, y, z = box
    answer = (x // n) * (y // n) * (z // n)
    return answer