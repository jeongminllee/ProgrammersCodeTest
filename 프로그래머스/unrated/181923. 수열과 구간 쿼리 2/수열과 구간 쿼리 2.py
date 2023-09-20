def solution(arr, queries):
    answer = []
    for query in queries :
        ans = []
        for i in range(query[0], query[1] + 1):
            if arr[i] > query[2] :
                ans.append(arr[i])
        try :
            answer.append(min(ans))
        except :
            answer.append(-1)
    return answer