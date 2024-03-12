def solution(a, b, n):
    answer = 0
    while n >= a :
        val = (n // a) * b
        answer += val
        n = val + n % a
    return answer