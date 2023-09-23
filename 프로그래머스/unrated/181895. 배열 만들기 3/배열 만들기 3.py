def solution(arr, intervals):
    answer = []
    for interval in intervals :
        interval0 = interval[0]
        interval1 = interval[1]
        
        for i in range(interval0, interval1 + 1) :
            answer.append(arr[i])
    return answer