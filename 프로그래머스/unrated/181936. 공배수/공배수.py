def solution(number, n, m):
    return int(not(number % n and number % m))

# def solution(num, n, m) :
#   return int(not(num % n and num % m))

# def solution(number, n, m):
#     return int(bool(number % n == 0) & bool(number % m == 0))

# def solution(number, n, m):
#     answer = 0
#     if number % n == 0 and number % m == 0 :
#         answer = 1
#     else :
#         answer = 0
#     return answer
