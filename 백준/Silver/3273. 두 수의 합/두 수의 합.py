from typing import List


N = int(input())
nums = list(map(int, input().split()))
target = int(input())

def twoSum(nums : List[int], target : int) -> List[int] :
    ans = 0
    hashtable_dict = {}
    for i in range(len(nums)) :
        value = target - nums[i]

        if hashtable_dict.get(value) is not None and hashtable_dict[value] != i :
            ans += 1

        hashtable_dict[nums[i]] = i

    return ans

print(twoSum(nums, target))