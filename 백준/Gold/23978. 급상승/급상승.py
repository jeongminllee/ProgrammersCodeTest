def sum_val(x) :
    return (x * (x + 1)) // 2

def can(target, nums, K):
    res = sum_val(target)
    for num in nums :

        res += sum_val(target) - sum_val(max(0, target - num))
        if res >= K :
            return True

    return res >= K

def find_minimum_X(N, K, dates):
    left = 1
    right = K  # 최대값으로 K를 설정
    diff = [dates[i+1] - dates[i] for i in range(N-1)][::-1]

    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2

        if can(mid, diff, K) :
            right = mid - 1
        else :
            left = mid + 1

    return left

def main() :
    # 입력 처리
    N, K = map(int, input().split())
    dates = list(map(int, input().split()))

    # 결과 출력
    result = find_minimum_X(N, K, dates)
    print(result)
    
main()