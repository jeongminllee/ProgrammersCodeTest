MAX_VAL = 2097152
tree = [0] * (MAX_VAL * 2)
ans = []

N = int(input())
for _ in range(N) :
    T, X = map(int, input().split())
    if T == 1 :
        idx = X + MAX_VAL - 1
        while idx :
            tree[idx] += 1
            idx >>= 1

    else :
        idx = 1
        tree[idx] -= 1
        while idx < MAX_VAL :
            left = idx * 2
            right = idx * 2 + 1
            if X > tree[left] :
                X -= tree[left]
                idx = right
            else :
                idx = left
            tree[idx] -= 1
        ans.append(idx - MAX_VAL + 1)

for a in ans :
    print(a)