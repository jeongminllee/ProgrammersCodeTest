def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer

# def solution(arr, idx):
#     answer = -1
#     for i in range(idx-1, len(arr)) :
#         if arr[i] == 1 :
#             if i >= idx :
#                 answer = i
#                 break
#     return answer
