def solution(s):
    answer = ''
    s = sorted(s)
    print(s)
    for i, a in enumerate(s) :
         if s.count(a) == 1 :
                answer += a
    return answer