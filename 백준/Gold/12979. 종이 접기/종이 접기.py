def min_folds_needed(L, target):
    """
    L에서 target까지 줄이기 위해 필요한 최소 접기 횟수를 구한다.
    한 번 접으면 최대로 많이 줄일 수 있는 값은 ceil(L/2)이다.
    target이 L보다 클 수는 없으므로, 만약 target > L이면 매우 큰 값을 반환한다.
    """
    if target > L:
        return float('inf')
    folds = 0
    current = L
    # current가 target보다 작거나 같아질 때까지 최적으로 접었을 때의 값으로 갱신한다.
    while current > target:
        current = (current + 1) // 2  # ceil(current/2)
        folds += 1
    return folds

def solve():
    W, H, A = map(int, input().split())

    # 만약 A가 원래 종이의 넓이보다 크면 접어서 A를 만들 수 없다.
    if A > W * H:
        print(-1)
        return

    # 원래 종이의 넓이가 이미 A라면 접을 필요가 없다.
    if A == W * H:
        print(0)
        return

    best = float('inf')
    found = False
    # A의 약수 쌍 (w, h)를 모두 찾는다.
    for d in range(1, int(A ** (1/2)) + 1):
        if A % d != 0:
            continue
        e = A // d
        # 후보 1: 최종 크기가 (d, e)가 되어야 하는 경우.
        if d <= W and e <= H:
            folds_w = min_folds_needed(W, d)
            folds_h = min_folds_needed(H, e)
            candidate = folds_w + folds_h
            if candidate < best:
                best = candidate
                found = True
        # 후보 2: (e, d)인 경우 (d와 e가 다르면 회전한 경우)
        if d != e:
            if e <= W and d <= H:
                folds_w = min_folds_needed(W, e)
                folds_h = min_folds_needed(H, d)
                candidate = folds_w + folds_h
                if candidate < best:
                    best = candidate
                    found = True
                    
    if found:
        print(best)
    else:
        print(-1)

if __name__ == '__main__':
    solve()