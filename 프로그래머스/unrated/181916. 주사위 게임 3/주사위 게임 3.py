def solution(a, b, c, d):
    answer = 0
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4 :
        answer = 1111 * a
        
    elif max(counts) == 3 :
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        answer = (10 * p + q) ** 2
        
    elif max(counts) == 2 :
        if min(counts) == 2 :
            answer = (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else :
            p = nums[counts.index(2)]
            answer = (a * b * c * d) / (p**2)
            
    else : 
        answer = min(nums)
        
    return answer