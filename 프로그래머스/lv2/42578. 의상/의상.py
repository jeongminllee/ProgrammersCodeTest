def solution(clothes):
    answer = 1
    c = {v[1] : [] for v in clothes}
    for clo in clothes :
        c[clo[1]].append(clo[0])
    for k in c.keys() :
        n = len(c[k])
        answer *= (n + 1)
        
    return answer - 1