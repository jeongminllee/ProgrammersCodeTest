import numpy as np

def solution(num_list, n):
    answer = np.array(num_list).reshape(-1, n)
    return answer.tolist()

# def solution(num_list, n):
#     answer = []
#     for i in range(0, len(num_list), n) :
#         answer.append(num_list[i:i + n])
        
#     return answer