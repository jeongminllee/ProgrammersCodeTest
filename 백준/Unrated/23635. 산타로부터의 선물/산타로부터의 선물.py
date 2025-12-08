INF = 10 ** 9

def bisect_left(a:list, x, lo=0, hi=None) :
    if hi is None :
        hi = len(a)

    while lo < hi :
        mid = (lo + hi) // 2

        if a[mid] >= x :
            hi = mid
        else :
            lo = mid + 1
            
    return lo

def calc(m) :
    pos = 0             # 현재까지 쓴 선물 인덱스 (prefix 기준, 0~N)
    for _ in range(K) :
        target = prefix[pos] + m    # 이번 아이는 최소 m 이상 받아야 함.
        idx = bisect_left(prefix, target, pos+1)    # prefix[idx] >= target인 최소 idx

        if idx > N :        # 못 만들면 이  m으로는 불가능
            return None
        pos = idx

    # pos번째 선물까지 사용함 -> 총 합
    return prefix[pos]

def main() :
    global K, N, prefix
    K, N = map(int, input().split())    # 아이 수, 선물 개수
    A = list(map(int, input().split())) # i번 선물의 기쁨 수치

    prefix = [0] * (N+1)
    for i in range(N) :
        prefix[i+1] = prefix[i] + A[i]

    total = prefix[N]
    max_m = total // K
    res = INF

    for m in range(1, max_m + 1) :
        T = calc(m)
        if T is None :
            continue
        res = min(res, T - K * m)

    print(res)

if __name__ == "__main__" :
    main()