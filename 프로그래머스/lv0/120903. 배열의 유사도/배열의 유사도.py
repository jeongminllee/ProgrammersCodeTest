# def solution(s1, s2):
#     answer = 0
#     for s in s1 :
#         if s in s2 :
#             answer += 1
#     return answer

def solution(s1, s2) :
    return len(set(s1) & set(s2))