def solution(nums):
    # choice = ((len(nums) - 1) // 2) + 1
    # nums 항상 짝수로만 주어짐
    choice = len(nums) // 2
    num = []
    for n in nums :
        if n not in num :
            num.append(n) 
    return min(len(num), choice)