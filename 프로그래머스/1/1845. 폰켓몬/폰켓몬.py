def solution(nums):
    n1 = len(nums) // 2
    n2 = len(set(nums))
    return min(n1, n2)