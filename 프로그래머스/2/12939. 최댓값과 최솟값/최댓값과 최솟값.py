def solution(s):
    lst = s.split()
    mn, mx = int(lst[0]), int(lst[0])
    
    for num in lst :
        num = int(num)
        mn = min(mn, num)
        mx = max(mx, num)
    
    return f"{mn} {mx}"