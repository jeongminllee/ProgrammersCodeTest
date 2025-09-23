def solution(s):
    stack = []
    for a in s :
        if a == '(' :
            stack.append('(')
        else :
            if not stack :
                return False
            stack.pop()
            
    if stack :
        return False
    else :
        return True