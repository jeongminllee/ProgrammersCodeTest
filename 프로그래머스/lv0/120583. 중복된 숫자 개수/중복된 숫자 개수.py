def solution(array, n):
    for i in array :
        if i == n :
            return array.count(i)
    return 0