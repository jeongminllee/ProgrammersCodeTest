def solution(num, total):
    lst = [i for i in range(-101, 101)]

    for i in lst :
        answer = lst[i : i + num]
        if sum(answer) == total :
            return answer