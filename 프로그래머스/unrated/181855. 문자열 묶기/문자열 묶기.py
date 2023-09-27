def solution(strArr):
    a = [len(i) for i in strArr]
    b = []
    
    for i in set(a) :
        b.append(a.count(i))
        
    return max(b)