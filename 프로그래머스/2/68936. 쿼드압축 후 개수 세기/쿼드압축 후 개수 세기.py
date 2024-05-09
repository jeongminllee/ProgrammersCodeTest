def compression(arr, answer, a, b, l) :
    start = arr[a][b]
    for i in range(a, a + l) :
        for j in range(b, b + l) :
            if arr[i][j] != start :
                l //= 2
                compression(arr, answer, a, b, l)
                compression(arr, answer, a+l, b, l)
                compression(arr, answer, a, b+l, l)
                compression(arr, answer, a+l, b+l, l)
                return 
    answer[start] += 1
            
def solution(arr):
    answer = [0, 0]
    n = len(arr)

    compression(arr, answer, 0, 0, n)
    return answer