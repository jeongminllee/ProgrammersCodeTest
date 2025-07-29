def solution(clothes):
    res = {v[1] : [] for v in clothes}
    for cloth, parts in clothes :
        res[parts].append(cloth)
        
    ans = 1
    
    for k in res.keys() :
        n = len(res[k])
        ans *= (n + 1)
    
    return ans - 1