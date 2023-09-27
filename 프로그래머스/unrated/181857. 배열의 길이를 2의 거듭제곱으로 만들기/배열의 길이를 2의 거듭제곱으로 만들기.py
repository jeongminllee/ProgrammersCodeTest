# def solution(arr):
#     cnt = 0
#     while len(arr) != pow(2, cnt) :
#         if len(arr) == pow(2, cnt) :
#             break
#         elif len(arr) > pow(2, cnt) :
#             cnt += 1
#         else :
#             chan = pow(2, cnt) - len(arr) 
#             for _ in range(chan) :
#                 arr.append(0)
    
#     return arr

def solution(arr) :
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
        
    return arr + [0] * (a - b)