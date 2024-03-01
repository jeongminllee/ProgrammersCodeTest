def solution(n) :
    answer = 0
    rev_num = []

    while n > 0:
        rev_num.append(n % 3)
        n //= 3
    # print(rev_num)  # [0, 0, 2, 1]

    # print(rev_num[::-1]) => [1, 2, 0, 0] 45 3진법 1200
    # 원래라면 이렇게 뒤집어야 함. 그러나 애초에 뒤집기 이기 때문에 그냥 받겠음.

    for i in range(len(rev_num)) :
        answer += ((3 ** (len(rev_num) - i - 1)) * rev_num[i])
        print(answer)   # 0, 0, 6, 7

    return answer