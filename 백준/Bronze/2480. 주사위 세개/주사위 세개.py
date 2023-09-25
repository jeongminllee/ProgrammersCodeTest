a, b, c = map(int, input().split())

nums = [a, b, c]
counts = [nums.count(i) for i in nums]

if max(counts) == 3 :
    print(10000 + a * 1000)
elif max(counts) == 2 :
    p = nums[counts.index(2)]
    q = nums[counts.index(1)]
    print(1000 + p * 100)
else :
    print(max(nums) * 100)