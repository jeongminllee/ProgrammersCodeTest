def solution(arr):
    answer = []
    i = 0
    stk = []
    for i in range(len(arr)) :
        if stk == [] :
            stk.append(arr[i])
            i += 1
        elif stk != [] and stk[-1] == arr[i] :
            stk.pop()
            i += 1
        elif stk != [] and stk != arr[i] :
            stk.append(arr[i])
            i += 1
            
    if stk == [] :
        stk = [-1]
            
    return stk