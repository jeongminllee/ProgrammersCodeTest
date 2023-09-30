# def solution(picture, k):
#     answer = []
#     for row in picture :
#         resized = ''
        
#         for pixel in row :
#             resized += pixel * k
            
#         for _ in range(k) :
#             answer.append(resized)
            
#     return answer

def solution(picture, k) :
    answer = []
    for i in range(len(picture)) :
        for _ in range(k) :
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x'*k))
            
    return answer