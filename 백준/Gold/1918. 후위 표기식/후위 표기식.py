def precedence(operator) :
    if operator in ('*', '/') :
        return 2
    elif operator in ('+', '-') :
        return 1
    return 0

def infix_to_postfix(expression) :
    res = []
    stack = []

    for char in expression :
        if char.isalpha() :
            res.append(char)
        elif char == '(' :
            stack.append(char)
        elif char == ')' :
            while stack and stack[-1] != '(' :
                res.append(stack.pop())
            stack.pop() # '(' 제거
        else :  # 연산자인 경우
            while stack and precedence(stack[-1]) >= precedence(char) :
                res.append(stack.pop())
            stack.append(char)

    while stack :
        res.append(stack.pop())

    return ''.join(res)

S = input()
print(infix_to_postfix(S))