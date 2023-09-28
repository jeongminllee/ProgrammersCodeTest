def solution(arr, delete_list):
    answer = []
    for i in arr :
        for j in delete_list :
            if i not in delete_list :
                if i not in answer :
                    answer.append(i)
    return answer