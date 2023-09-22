def solution(n, slicer, num_list):
    answer = []
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    
    if n == 1 :
        a = 0
        c = 1
    elif n == 2 :
        b = len(num_list)
        c = 1
    elif n == 3 :
        c = 1
    else :
        a = a
        b = b
        c = c
    
    answer = num_list[a : b + 1 : c]
    return answer