def solution(s):
    res = ''
    
    for i in range(len(s)) :
        if not s[i].isalpha() :
            res += s[i]
        elif (i==0 or s[i-1] == ' ') and s[i].isalpha() :
            res += s[i].upper()
        else :
            res += s[i].lower()
            
    return res