def calculate_total_money(N, dates, X):
    total = 0
    for i in range(N) :
        current_date = dates[i]
        next_date = dates[i + 1] if i < N - 1 else float('inf')
        days = next_date - current_date

        if days >= X :
            # X 부터 1까지의 합 : X * (X+1) // 2
            total += (X * (X + 1)) // 2
        else :
            # X 부터 (X - days + 1) 까지의 합
            # 첫 항 : X, 마지막 항 : (X - days + 1), 항의 개수 : days
            first = X
            last = X - days + 1
            total += (first + last) * days // 2

    return total

def find_minimum_X(N, K, dates):
    left = 1
    right = K  # 최대값으로 K를 설정

    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2
        total_money = calculate_total_money(N, dates, mid)

        if total_money >= K:
            right = mid - 1
        else:
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

'''
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
'''
