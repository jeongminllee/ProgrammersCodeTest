def solution(nums):
    n = len(nums)
    nums = set(nums)
    return (min(n//2, len(nums)))