def solution(nums):
    n = len(nums)
    nums = set(nums)
    answer = min(n//2, len(nums))
    return answer