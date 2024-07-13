# def solution(num, total):
#     d = 0
#     for i in range(num) :
#         d += i
#     start = (total - d) // num
#     answer = [i for i in range(start, start + num)]
        
#     return answer

def solution(num, total):
    # 연속된 숫자의 시작값을 계산
    start = (total - sum(range(num))) // num
    
    # 시작값부터 num개의 연속된 숫자를 리스트로 만들어 반환
    return list(range(start, start + num))