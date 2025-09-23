def solution(s):
    res = ''
    
    for i in range(len(s)) :
        if not s[i].isalpha() :
            res += s[i]
        else :
            if (s[i-1] == ' ' or i == 0) and s[i].isalpha() :
                res += s[i].upper()
            elif s[i].isalpha() :
                res += s[i].lower()
                
    return res