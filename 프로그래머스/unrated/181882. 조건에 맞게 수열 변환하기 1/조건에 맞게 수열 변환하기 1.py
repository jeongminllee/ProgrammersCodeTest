def solution(arr):
    return [i*2 if i < 50 and i % 2 == 1 else(i/2 if i >= 50 and i % 2 == 0 else i) for i in arr]

def solution(arr) :
    for i, val in enumerate(arr) :
        if val < 50 and val % 2 == 1 :
            val *= 2
            arr[i] = val
        elif val >= 50 and val % 2 == 0 :
            val /= 2
            arr[i] = val
        else :
            arr[i] = val
    return arr