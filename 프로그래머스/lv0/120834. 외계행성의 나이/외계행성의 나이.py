def solution(age):
    answer = ''
    alist = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    a = list(map(int, str(age)))
    for i in a :
        answer += alist[int(i)]
        
    return answer