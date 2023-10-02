def solution(num, k):
    nums = str(num)
    for n in nums :
        if n == str(k) :
            return nums.index(n) + 1
    return -1
        