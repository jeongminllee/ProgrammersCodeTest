# solution = lambda a, n:sorted(a, key=lambda x:(abs(x-n), x))[0]


def solution(array, n) :
    array.sort(key = lambda x: (abs(x-n), x-n))
    answer = array[0]
    return answer