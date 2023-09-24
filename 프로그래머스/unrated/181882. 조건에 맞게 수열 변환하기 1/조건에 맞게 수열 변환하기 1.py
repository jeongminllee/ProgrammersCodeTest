def solution(arr):
    for idx, val in enumerate(arr) :
        if val % 2 == 1 and val < 50 :
            val *= 2
            arr[idx] = val
        elif val % 2 == 0 and val >= 50 :
            val /= 2
            arr[idx] = val
        else :
            arr[idx] = val
    return arr