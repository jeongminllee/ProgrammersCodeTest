class StackDef:
    def push(stack, value):
        stack.append(value)
        return stack
    
    def pop(stack, result):
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(int(stack[-1]))
            stack.pop()
        return stack, result
    
    def size(stack, result):
        result.append(len(stack))
        return stack, result
    
    def empty(stack, result):
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
        return stack, result
    
    def top(stack, result):
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(int(stack[-1]))
        return stack, result


stack = []
result = []
for i in range(int(input())):
    inputValue = input().split(" ")
    if len(inputValue) == 1:
        stack, result = getattr(StackDef, inputValue[0])(stack, result)
    else:
        stack = getattr(StackDef, inputValue[0])(stack, inputValue[1])
    
for j in result:
    print(j)