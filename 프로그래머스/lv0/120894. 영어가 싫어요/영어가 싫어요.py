def solution(numbers):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    for i in range(len(num_list)) :
        numbers = numbers.replace(num_list[i], str(i))
    return int(numbers)