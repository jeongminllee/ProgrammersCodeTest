def is_prime(n) :
    if n <= 1 :
        return False
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    result = []
    for i in range(len(nums) - 2) :
        for j in range(i + 1, len(nums) - 1) :
            for k in range(j + 1, len(nums)) :
                    result.append(nums[i] + nums[j] + nums[k])
    for i in range(len(result)) :
        if is_prime(result[i]) :
            answer += 1
    return answer if result else -1