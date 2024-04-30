def solution(n):
    answer = []

    def hanoi(n, from_, to_, via_) :
        if n == 1 :
            answer.append([from_, to_])
        else :
            hanoi(n-1, from_, via_, to_)
            # hanoi(1, from_, to_, via_)
            answer.append([from_, to_])
            hanoi(n-1, via_, to_, from_)
    hanoi(n, 1, 3, 2)
    return answer

    return answer