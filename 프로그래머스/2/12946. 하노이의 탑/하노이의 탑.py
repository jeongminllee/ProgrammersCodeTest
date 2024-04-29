def solution(n):
    answer = []

    def hanoi(src, dst, inter, n) :
        if n == 1 :
            answer.append([src, dst])
        else :
            hanoi(src,inter,dst,n-1)
            hanoi(src, dst, inter, 1)
            hanoi(inter, dst, src, n - 1)
    hanoi(1, 3, 2, n)

    return answer