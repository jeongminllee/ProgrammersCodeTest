def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

# def solution(left, right):
#     answer = 0
#     for i in range(left, right + 1) :
#         lst = []
#         for j in range(1, right + 1) :
#             if i % j == 0 :
#                 lst.append(j)
#         if len(lst) % 2 == 0 :
#             answer += i
#         else :
#             answer -= i
#     return answer