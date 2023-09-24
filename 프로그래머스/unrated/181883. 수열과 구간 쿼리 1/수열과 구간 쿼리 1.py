def solution(arr, queries):
    for i in queries :
        a = [x + 1 for x in arr[i[0] : i[1] + 1]]
        arr[i[0] : i[1] + 1] = a
    return arr