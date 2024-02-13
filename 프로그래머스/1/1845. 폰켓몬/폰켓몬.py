def solution(nums):
    # choice = ((len(nums) - 1) // 2) + 1
    # nums 항상 짝수로만 주어짐
    k = len(nums) // 2
    num = set(nums)
    return min(len(num), k)