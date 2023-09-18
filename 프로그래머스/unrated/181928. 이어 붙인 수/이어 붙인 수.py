def solution(num_list):
    answer = 0
    num1 = ''
    num2 = ''
    for num in num_list :
        if num % 2 == 1 :
            num1 += str(num)
        else :
            num2 += str(num)
    answer = int(num1) + int(num2)
    return answer