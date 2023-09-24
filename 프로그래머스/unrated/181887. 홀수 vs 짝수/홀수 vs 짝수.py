def solution(num_list):
    for i in range(len(num_list)) :
        num1 = sum(num_list[i :: 2])
        num2 = sum(num_list[i+1 :: 2])
        print(num1)
        print(num2)
        if num1 > num2 :
            return num1
        else :
            return num2
